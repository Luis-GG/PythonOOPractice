"""Python serial number generator."""


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
        """initialize values and keep track of initial start value"""
        self.start = start
        self.initial_val = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.start + 1}>"

    def generate(self):
        """initialy returns the given start value and then every time generate is called, return the next sequential number"""
        self.start += 1
        return self.start-1

    def reset(self):
        """resets the start value to the initial start value that was provided"""
        self.start = self.initial_val
