"""Module for Affine cipher"""

from itertools import product
from cipher import Cipher
from caesar import Caesar
from multiplication import Multiplication


class Affine(Cipher):
    """Implements cipher via the affine method"""

    def __init__(self, key, alphabet_size):
        super().__init__("Affine", alphabet_size, key)
        mkey, ckey = key
        self.multiplication = Multiplication(mkey, alphabet_size)
        self.caesar = Caesar(ckey, alphabet_size)

    def encode(self, message):
        caesared = self.caesar.encode(message)
        multiplied = self.multiplication.encode(caesared)
        return multiplied

    def decode(self, encrypted):
        multiplied = self.multiplication.decode(encrypted)
        caesared = self.caesar.decode(multiplied)
        return caesared

    def candidate_keys(self):
        caesar_candidates = self.caesar.candidate_keys()
        multiplication_candidates = self.multiplication.candidate_keys()

        return product(multiplication_candidates, caesar_candidates)

    @staticmethod
    def generate_key(alphabet_size):
        return Multiplication.generate_key(alphabet_size), Caesar.generate_key(alphabet_size)
