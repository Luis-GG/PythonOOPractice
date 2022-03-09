"""Word Finder: finds random words from a dictionary."""


from asyncore import loop
import random


class WordFinder:

    def __init__(self, path):
        word_file = open(path, "r")
        self.words = self.parse(word_file)
        print(f"{len(self.words)} words read")

    def parse(self, word_file):
        parsed_list = []

        for words in word_file:
            parsed_list.append(words.strip())
        return parsed_list

    def random(self):
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):

    def parse(self, word_file):
        parsed_list = []

        for words in word_file:
            if words.strip() and not words.startswith("#"):
                parsed_list.append(words.strip())

        return parsed_list
