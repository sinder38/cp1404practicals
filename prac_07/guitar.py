"""
CP1404/CP5632 Practical
Guitar
"""

from datetime import datetime

VINTAGE_AGE = 50


class Guitar:
    """Stores information about a guitar"""

    def __init__(self, name="", year=0, cost=0):
        """Construct a Guitar class instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar class"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, year_override=None):
        """Get the age of a guitar based on the current year"""
        # NOTE: Using a constant for a year as done in the solution is a bad idea
        # that will make program wrong only after a year. So:
        if year_override is None:
            current_year = datetime.now().year
        else:
            current_year = year_override
        return current_year - self.year

    def is_vintage(self, year_override=None):
        """Determine if a Guitar is vintage"""
        return self.get_age(year_override) >= VINTAGE_AGE
