import filecmp
import os

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


def encrypt_file(source_plaintext_filename, ciphertext_filename, key_id):
    """
    Encrypts a file using an AWS KMS master key provider and a custom static master key provider.
    :param key_id: Key ID of the AWS KMS CMK
    :param ciphertext_filename: Output filename for encrypted file
    :param source_plaintext_filename:  Filename of file to encrypt
    """
    client = aws_encryption_sdk.EncryptionSDKClient(commitment_policy=CommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT)

    # create a static random master key provider
    master_key_provider = StaticRandomMasterKeyProvider()
    master_key_provider.add_master_key(key_id)

    try:
        # Encrypt the file
        with open(source_plaintext_filename, "rb") as source_plaintext, open(ciphertext_filename, "wb") as ciphertext:
            with client.stream(
                algorithm=Algorithm.AES_256_GCM_HKDF_SHA512_COMMIT_KEY,
                source=source_plaintext,
                mode="e",
                key_provider=master_key_provider
            ) as encryptor:
                for chunk in encryptor:
                    ciphertext.write(chunk)
        return True, master_key_provider
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


