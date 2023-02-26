import hashlib
import json
import os
from base64 import b64encode

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad


class EncryptionTool:
    def __init__(self, user_file, user_key, file_id, output_file):
        self.user_file = user_file

        self.input_file_size = os.path.getsize(self.user_file)
        self.chunk_size = 1024 * 1024 * 500
        self.total_chunks = self.input_file_size // self.chunk_size + 1

        # convert the key and salt to bytes
        self.user_key = bytes(user_key, "utf-8")
        self.user_salt = bytes(user_key[::-1], "utf-8")
        self.file_id = file_id

        # get the file extension
        self.file_extension = self.user_file.split(".")[-1]

        self.hash_type = "SHA256"

        # encrypted file name

        self.encrypt_output_file = output_file

        # dictionary to store hashed key and salt

        self.hashed_key_salt = dict()
        # hash key and salt into 16 bit hashes

        self.hash_key_salt()

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
        cipher = AES.new(
            self.hashed_key_salt["key"], AES.MODE_OFB
        )

        self.abort()  # if the output file already exists, remove it first

        input_file = open(self.user_file, "rb")

        ciphertext = b''
        for piece in self.read_in_chunks(input_file, self.chunk_size):
            ciphertext += cipher.encrypt(piece)
        input_file.close()
        json_k = ['iv', 'ciphertext', 'extra']
        json_v = [b64encode(x).decode('utf-8') for x in (cipher.iv, ciphertext, self.file_id)]
        result = bytes(json.dumps(dict(zip(json_k, json_v))), encoding="utf-8")

        total_chunks = len(result)//self.chunk_size + 1
        done_chunks = 0
        with open(self.encrypt_output_file, "ab") as f:
            offset = 0
            while offset < len(result):
                f.write(result[offset:offset+self.chunk_size])
                offset += self.chunk_size
                done_chunks += 1
                yield done_chunks / total_chunks * 100

        del cipher
        del result

    def abort(self):
        if os.path.isfile(self.encrypt_output_file):
            os.remove(self.encrypt_output_file)

    def hash_key_salt(self):

        # --- convert key to hash
        #  create a new hash object

        hasher = hashlib.new(self.hash_type)
        hasher.update(self.user_key)

        # turn the output key hash into 32 bytes (256 bits)

        self.hashed_key_salt["key"] = bytes(hasher.hexdigest()[:32], "utf-8")

        # clean up hash object

        del hasher

        # --- convert salt to hash
        #  create a new hash object

        hasher = hashlib.new(self.hash_type)
        hasher.update(self.user_salt)

        # turn the output salt hash into 16 bytes (128 bits)

        self.hashed_key_salt["salt"] = bytes(hasher.hexdigest()[:16], "utf-8")

        # clean up hash object

        del hasher
