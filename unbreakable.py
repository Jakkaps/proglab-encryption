"""Moduel for Unbreakable class"""

from random import randint
from itertools import product
from cipher import Cipher
from ascii_helper import to_num, to_char


class Unbreakable(Cipher):
    """Unbreakable cipher. Works by combining Caesar and Multiplication cipher"""

    def __init__(self, key, alphabet_size):
        super().__init__("Unbreakable", alphabet_size, key)

    def encode(self, message):
        # Get a repeating key of the same length as the message
        key_letters = []
        if len(message) < len(self.key):
            key_letters = self.key[:len(message)]
        else:
            i = 0
            for _ in range(len(message)):
                key_letters.append(self.key[i])
                i += 1
                if i >= len(self.key):
                    i = 0
        correct_length_key = ''.join(key_letters)
        self.key_as_nums = self.__str_to_nums(correct_length_key)

        return self.__encrypt(message, self.key_as_nums)

    def __encrypt(self, message, key):
        message_as_nums = self.__str_to_nums(message)
        ascii_nums = [(key[i] + message_as_nums[i]) for i in range(len(message))]
        encrypted = "".join([to_char(num) for num in ascii_nums])

        return encrypted

    @staticmethod
    def __str_to_nums(string):
        return [to_num(c) for c in string]

    def decode(self, encrypted):
        # Get repeating key that matches encrypt key
        key = [(self.alphabet_size - self.key_as_nums[i]) %
               self.alphabet_size for i in range(len(self.key_as_nums))]
        return self.__encrypt(encrypted, key)

    def candidate_keys(self):
        keys = []
        possible_asciis = [to_char(i) for i in range(96)]
        for i in product(possible_asciis, repeat=1):
            keys.append(''.join(i))

        return keys

    @staticmethod
    def generate_key(alphabet_size):
        return "".join([to_char(randint(0, alphabet_size)) for _ in range(1)])
