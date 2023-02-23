import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

import aws_encryption_sdk
from aws_encryption_sdk.key_providers.raw import RawMasterKeyProvider
from aws_encryption_sdk.identifiers import Algorithm, CommitmentPolicy, EncryptionKeyType, WrappingAlgorithm
from aws_encryption_sdk.internal.crypto.wrapping_keys import WrappingKey


class StaticRandomMasterKeyProvider(RawMasterKeyProvider):
    """Randomly generates and provides 4096-bit RSA keys consistently per unique key id."""

    provider_id = "static-random"

    def __init__(self, **kwargs):  # pylint: disable=unused-argument
        """Initialize empty map of keys."""
        self._static_keys = {}

    def _get_raw_key(self, key_id):
        """Retrieves a static, randomly generated, RSA key for the specified key id.

        :param str key_id: User-defined ID for the static key
        :returns: Wrapping key that contains the specified static key
        :rtype: :class:`aws_encryption_sdk.internal.crypto.WrappingKey`
        """
        try:
            static_key = self._static_keys[key_id]
        except KeyError:
            private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096, backend=default_backend())
            static_key = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption(),
            )
            self._static_keys[key_id] = static_key
        return WrappingKey(
            wrapping_algorithm=WrappingAlgorithm.RSA_OAEP_SHA1_MGF1,
            wrapping_key=static_key,
            wrapping_key_type=EncryptionKeyType.PRIVATE,
        )


def encrypt_file(key_arn, source_plaintext_filename, ciphertext_filename, key_id, botocore_session=None):
    """
    Encrypts a file using an AWS KMS master key provider and a custom static master key provider.
    :param key_id: Key ID of the AWS KMS CMK
    :param ciphertext_filename: Output filename for encrypted file
    :param source_plaintext_filename:  Filename of file to encrypt
    """
    client = aws_encryption_sdk.EncryptionSDKClient(commitment_policy=CommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT)

    # Create an AWS KMS master key provider
    kms_kwargs = dict(key_ids=[key_arn])
    if botocore_session is not None:
        kms_kwargs["botocore_session"] = botocore_session
    kms_master_key_provider = aws_encryption_sdk.StrictAwsKmsMasterKeyProvider(**kms_kwargs)

    static_key_id = os.urandom(8)
    static_master_key_provider = StaticRandomMasterKeyProvider()
    static_master_key_provider.add_master_key(static_key_id)
    kms_master_key_provider.add_master_key_provider(static_master_key_provider)

    try:
        # Encrypt the file
        with open(source_plaintext_filename, "rb") as source_plaintext, open(ciphertext_filename, "wb") as ciphertext:
            with client.stream(
                    algorithm=Algorithm.AES_256_GCM_HKDF_SHA512_COMMIT_KEY,
                    source=source_plaintext,
                    mode="e",
                    key_provider=key_id
            ) as encryptor:
                for chunk in encryptor:
                    ciphertext.write(chunk)
        return True, key_id
    except Exception as e:
        print(e)
        return False, "Encryption Error"


def decrypt_file(source_plaintext_filename, key_id):
    # master_key_provider = StaticRandomMasterKeyProvider()
    # master_key_provider.add_master_key(key_id)
    # decrypt the ciphertext
    master_key_provider = StaticRandomMasterKeyProvider()
    master_key_provider.add_master_key(key_id)
    cycled_plaintext_filename = source_plaintext_filename.split(".")[0] + ".mp4"
    client = aws_encryption_sdk.EncryptionSDKClient(commitment_policy=CommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT)

    try:
        with open(source_plaintext_filename, "rb") as ciphertext, open(cycled_plaintext_filename, "wb") as plaintext:
            with client.stream(mode="decrypt-unsigned", source=ciphertext,
                               key_provider=master_key_provider) as decryptor:
                for chunk in decryptor:
                    plaintext.write(chunk)
        return True, "Decryption successfully"
    except Exception as e:
        print(e)
        return False, "Decryption Error"


class EncryptionTool:
    def __init__(self, user_file, user_key, output_file):
        self.user_file = user_file

        self.input_file_size = os.path.getsize(self.user_file)
        self.chunk_size = 1024 * 1024 * 200
        self.total_chunks = self.input_file_size // self.chunk_size + 1

        # convert the key and salt to bytes
        self.user_key = bytes(user_key, "utf-8")
        self.user_salt = bytes(user_key[::-1], "utf-8")

        # get the file extension
        self.file_extension = self.user_file.split(".")[-1]

        self.hash_type = "SHA256"

        # encrypted file name

        self.encrypt_output_file = output_file

    @staticmethod
    def read_in_chunks(file_object, chunk_size):
        """Lazy function (generator) to read a file piece by piece.
        Default chunk size: 1k.
        """

        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data

    def encrypt(self):

        # create a cipher object
        # cipher_object = AES.new(
        #     self.hashed_key_salt["key"], AES.MODE_CFB, self.hashed_key_salt["salt"]
        # )
        fernet = Fernet(self.user_key)
        self.abort()  # if the output file already exists, remove it first

        input_file = open(self.user_file, "rb")
        output_file = open(self.encrypt_output_file, "ab")
        done_chunks = 0

        for piece in self.read_in_chunks(input_file, self.chunk_size):
            encrypted_content = fernet.encrypt(piece)
            output_file.write(encrypted_content)
            done_chunks += 1
            yield done_chunks / self.total_chunks * 100

        input_file.close()
        output_file.close()

        # clean up the cipher object

        del fernet

    def abort(self):
        if os.path.isfile(self.encrypt_output_file):
            os.remove(self.encrypt_output_file)
