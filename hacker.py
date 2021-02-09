"""Module for hacker class"""

import string


class Hacker:
    """Tries to decipher a message by testing all possible keys"""
    def __init__(self):
        """Initialize hacker with all english words"""
        with open('english_words.txt', 'r') as file:
            self.all_words = [w.strip() for w in file.readlines()]

    def brute_force(self, message, cipher):
        """Try to crack a message by testing all possible keys of cipher"""
        candidate_keys = cipher.candidate_keys()
        words_in_best_match = 0
        best_match = ''
        for key in candidate_keys:
            cipher.key = key
            decrypted = cipher.decode(message)
            matches = self.__matched_words(decrypted)
            if matches > words_in_best_match:
                words_in_best_match = matches
                best_match = decrypted

        if best_match:
            print(f"The hacker guesses that the message was '{best_match}'")
        else:
            print("The hacker is not able to decrypt the message")

        print("\n")

    def __matched_words(self, message):
        words = message.split(' ')
        matches = 0
        for word in words:
            # Remove punctionation and make lower
            word.translate(str.maketrans('', '', string.punctuation))
            word = word.lower()

            if word in self.all_words:
                matches += 1

        return matches
