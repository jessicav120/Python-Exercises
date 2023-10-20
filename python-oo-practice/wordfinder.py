"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """
    Finds random words from a dictionary file. 
    
    >>> wf = WordFinder("/home/jessicav120/Python/python-oo-practice/my_words.txt")
    9 words read

    >>> wf.words
    ['purple', 'green', 'cat', 'dog', 'love', 'hate', 'mothership', 'alien', 'simple']

    >>> wf.random() in wf.words
    True

    >>> wf.random() in wf.words
    True
    """
    def __init__(self, path):
        file = open(path, "r")

        self.words = self.make_word_list(file)

        print(f"{len(self.words)} words read")

        file.close()

    def make_word_list(self, file):
        return [word.strip() for word in file]
    
    def random(self):
        return choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """
    A Specialized Word Finder that excludes section titles and blank lines.

    >>> swf = SpecialWordFinder("/home/jessicav120/Python/python-oo-practice/my_special_words.txt")
    10 words read

    >>> swf.words
    ['cherry', 'banana', 'starfruit', 'apple', 'lettuce', 'spinach', 'kale', 'cucumber', 'yummy', 'yum']

    >>> swf.random() in swf.words
    True
    """

    def make_word_list(self, file):
        """Exludes blank lines and commented strings from word list"""
        return [word.strip() for word in file if word.strip() and not word.startswith("#")]