"""
CP1404/CP5632 Practical
UnreliableCar class
"""

from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """Unreliable version of a Car"""

    def __init__(self, name, fuel, reliability):
        """Initialise Unreliable Car instance, based on parent class Car"""
        super().__init__(name, fuel)
        self.reliability = reliability # Percentage (1-100)

    def drive(self, distance):
        """Drive the car with a chance of getting 0 depending on reliability"""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
