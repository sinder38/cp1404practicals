"""
CP1404/CP5632 Practical
Guitar
"""


class Guitar:
    """Stores information about a guitar"""

    def __init__(self, name="", year=0, cost=0):
        """Construct a Guitar class instance"""
        self.name = name
        self.year = year
        self.cost = cost
