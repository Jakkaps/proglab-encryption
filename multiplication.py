"""Module for Multiplication class"""
from random import randint
from cipher import Cipher
from ascii_helper import to_char, to_num
from crypto_utils import modular_inverse


class Multiplication(Cipher):
    """Extends Cipher by using the multiplication cipher"""
    def __init__(self, key, alphabet_size):
        super().__init__("Multiplication", alphabet_size, key)

    def encode(self, message):
        return self.__encrypt(message, self.key)

    def decode(self, encrypted):
        inverse = modular_inverse(self.key, self.alphabet_size)
        return self.__encrypt(encrypted, inverse)

    def __encrypt(self, message, key):
        ascii_nums = [to_num(c) for c in message]
        encrypted = "".join([to_char((num * key) % self.alphabet_size) for num in ascii_nums])
        return encrypted

    def candidate_keys(self):
        keys = []
        for i in range(self.alphabet_size):
            if (modular_inverse(i, self.alphabet_size) * i) % self.alphabet_size == 1:
                keys.append(i)
        return keys

    @staticmethod
    def generate_key(alphabet_size):
        potential_key = randint(0, alphabet_size)
        mod_inverse = modular_inverse(potential_key, alphabet_size)

        while (mod_inverse * potential_key) % alphabet_size != 1:
            potential_key = randint(0, alphabet_size)
            mod_inverse = modular_inverse(potential_key, alphabet_size)

        return potential_key
