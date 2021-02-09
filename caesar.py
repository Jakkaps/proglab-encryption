"""Module for Caesar class"""
from random import randint
from cipher import Cipher
from ascii_helper import to_num, to_char


class Caesar(Cipher):
    """Implements cipher with caesar method"""

    def __init__(self, key, alphabet_size):
        super().__init__("Caesar", alphabet_size, key)

    @staticmethod
    def generate_key(alphabet_size):
        return randint(0, alphabet_size)

    def candidate_keys(self):
        return range(self.alphabet_size)

    def encode(self, message):
        return self.__encrypt(self.key, message)

    def decode(self, encrypted):
        return self.__encrypt(self.alphabet_size - self.key, encrypted)

    def __encrypt(self, key, message):
        ascii_nums = [to_num(c) for c in message]
        encrypted_nums = [((num + key) % self.alphabet_size) for num in ascii_nums]
        encrypted = ''.join([to_char(num) for num in encrypted_nums])
        return encrypted
