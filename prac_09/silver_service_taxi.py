"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A fancy taxi with additional fees"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Taxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of SilverServiceTaxi"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the current fare"""
        return round(self.flagfall + super().get_fare(), 1)
