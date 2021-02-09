"""Module for person class and subclasses"""

from abc import ABC, abstractmethod
from cipher import Cipher


class Person(ABC):
    """Abstract person class"""

    def __init__(self, cipher: Cipher):
        self.cipher = cipher

    def print_cipher(self):
        """Prints name of cipher used"""
        print(self.cipher.name)

    @abstractmethod
    def operate_cipher(self, message):
        """Implemented by subclasses to use cipher for encryption of decryption"""
        raise NotImplementedError


class Receiver(Person):
    """Extends Person superclass to decrypt in operate_cipher"""

    def operate_cipher(self, message):
        decrypted = self.cipher.decode(message)
        print(f"I received {message}, which became '{decrypted}' when decrypted")


class Sender(Person):
    """Subclass of Person that overrides opperate_cipher to send a message"""

    def operate_cipher(self, message):
        """Sends message via self.cipher"""
        encrypted = self.cipher.encode(message)
        print(f"I sent the message '{message}', which became {encrypted} when encrypted")
        return encrypted
