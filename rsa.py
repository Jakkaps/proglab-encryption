"""Module for RSA class"""

from random import randint
from cipher import Cipher
from crypto_utils import generate_random_prime, modular_inverse, blocks_from_text, text_from_blocks


class RSA(Cipher):
    """RSA class. Implements RSA encryption with other instance of same class"""
    def __init__(self, own_private, partner_public, alphabet_size):
        super().__init__("RSA", alphabet_size, (own_private, partner_public))
        self.n_partner, self.e_partner = partner_public
        self.n_own, self.d_own = own_private

    def encode(self, message):
        decimal = blocks_from_text(message, 1)
        return [pow(c, self.e_partner, self.n_partner) for c in decimal]

    def decode(self, encrypted):
        decypted_decimals = [pow(c, self.d_own, self.n_own) for c in encrypted]
        print(f'Decimals decrypted: {decypted_decimals}')
        return text_from_blocks(decypted_decimals, 8)

    def candidate_keys(self):
        pass

    @staticmethod
    def generate_key(alphabet_size):
        num_bits = 8
        prime1 = generate_random_prime(num_bits)
        prime2 = generate_random_prime(num_bits)

        while prime1 == prime2:
            prime2 = generate_random_prime(num_bits)

        prime_factor = prime1 * prime2
        phi = (prime1 - 1) * (prime2 - 1)

        encrypt = decrypt = 0
        mod_found = False
        while not mod_found:
            encrypt = randint(3, phi - 1)
            decrypt = modular_inverse(encrypt, phi)
            mod_found = ((encrypt*decrypt) % phi == 1)

        public = (prime_factor, encrypt)
        private = (prime_factor, decrypt)

        return public, private
