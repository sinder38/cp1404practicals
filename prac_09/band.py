"""
CP1404/CP5632 Practical
Band class
"""


class Band:
    """Band Class"""

    def __init__(self, name=""):
        """Initialize Band Class"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band"""
        return f"{self.name} ({', '.join([str(musician) for musician in self.musicians])})"

    def add(self, musician):
        """Add a musician to the band"""
        self.musicians.append(musician)

    def play(self):
        """Call each of the band members to play"""
        return "\n".join((musician.play() for musician in self.musicians))
