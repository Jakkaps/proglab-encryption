"""Helper methods for ascii-translation with 95 charecters"""


def to_num(char):
    """Gets a number for a character"""
    return (ord(char) - 32) % 95


def to_char(num):
    """Gets a character from a number"""
    return chr((num % 95) + 32)
