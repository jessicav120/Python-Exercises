"""Python serial number generator."""
from itertools import count

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=100):
        """
        Initialize generator with starting value.

        Attributes
        --------------------
        self.start: int
            initial start value
        self.next: int
            value to be incremented by generator. Is initially the start value
        """
        self.start = start
        self.next = start

    def __repr__(self):
        return f"SerialGenerator start={self.start} next={self.next}"
    
    def generate(self):
        """Prints next serial number"""
        print(self.next)
        self.next += 1

    def reset(self):
        """Resets number to original start value"""
        self.next = self.start
