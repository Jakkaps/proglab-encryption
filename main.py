"""Main program for testing ciphers"""

from caesar import Caesar
from multiplication import Multiplication
from affine import Affine
from unbreakable import Unbreakable
from hacker import Hacker
from person import Sender, Receiver
from rsa import RSA

ALPHABET_SIZE = 95


def run_rsa(message):
    """Runs RSA-ciphers"""
    public1, private1 = RSA.generate_key(ALPHABET_SIZE)
    public2, private2 = RSA.generate_key(ALPHABET_SIZE)

    cipher1 = RSA(private1, public2, ALPHABET_SIZE)
    cipher2 = RSA(private2, public1, ALPHABET_SIZE)

    sender = Sender(cipher1)
    encrypted = sender.operate_cipher(message)

    receiver = Receiver(cipher2)
    receiver.operate_cipher(encrypted)


def run_normal_cipher(cipher, message):
    """Sends a message using cipher"""
    sender = Sender(cipher)
    encrypted = sender.operate_cipher(message)

    receiver = Receiver(cipher)
    receiver.operate_cipher(encrypted)

    hacker = Hacker()
    hacker.brute_force(encrypted, cipher)


def main():
    """Main program for testing ciphers"""
    key = Affine.generate_key(ALPHABET_SIZE)
    cipher = Affine(key, ALPHABET_SIZE)

    key = Multiplication.generate_key(ALPHABET_SIZE)
    cipher2 = Multiplication(key, ALPHABET_SIZE)

    key = Caesar.generate_key(ALPHABET_SIZE)
    cipher3 = Caesar(key, ALPHABET_SIZE)

    key = Unbreakable.generate_key(ALPHABET_SIZE)
    cipher4 = Unbreakable(key, ALPHABET_SIZE)

    # run_normal_cipher(cipher, "Test of affine")
    # run_normal_cipher(cipher2, "Test of multiplication")
    # run_normal_cipher(cipher3, "Test of caesar")
    run_normal_cipher(cipher4, "Test of unbreakable")

    run_rsa("Test of RSA")


if __name__ == '__main__':
    main()
