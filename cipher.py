"""Module for Cipher class"""
from abc import ABC, abstractmethod


class Cipher(ABC):
    """Cipher superclass. Extend to implement the actual logic of any given cipher"""
    alphabet_size = 95

    def __init__(self, name, alphabet_size, key):
        self.name = name
        self.alphabet_size = alphabet_size
        self.key = key

    def verify(self, message):
        """Tests that encode and decode on a message produces the original message"""
        encrypted = self.encode(message)
        decrypted = self.decode(encrypted)

        if message == decrypted:
            print(f'{self.name} cipher works as intended!')
        else:
            print(f'{self.name} does not work. Expected "{message}", got "{decrypted}"')

    @abstractmethod
    def encode(self, message):
        """Encode the message using some encryption method"""
        raise NotImplementedError

    @abstractmethod
    def candidate_keys(self):
        """Return all possible keys for this cipher"""
        raise NotImplementedError

    @abstractmethod
    def decode(self, encrypted):
        """Decode message using some decryption method"""
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def generate_key(alphabet_size):
        """Generate a key for this cipher"""
        raise NotImplementedError
