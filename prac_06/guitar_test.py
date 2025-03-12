from datetime import datetime

from prac_06.guitar import Guitar

def run_tests():
    """Tests for Guitar class"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40 # what

    guitar = Guitar(name, year, cost)
    other = Guitar("Guitar", 2013, 100)

    # get age datetime test

    current_year = datetime.now().year
    print(f"Current year: {current_year}")
    print(f"{guitar.name} get_age() - Expected {current_year-1922}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {current_year-2013}. Got {other.get_age()}")
    print()

    # get age override test
    current_year = 2025
    print(f"Set year: {current_year}")
    print(f"{guitar.name} get_age() - Expected {103}. Got {guitar.get_age(current_year)}")
    print(f"{other.name} get_age() - Expected {12}. Got {other.get_age(current_year)}")
    print()

    # vintage datetime test
    current_year = datetime.now().year
    vintage_age = 50
    print(f"Set year: {current_year}")
    print(f"{guitar.name} is_vintage() - Expected {current_year-1922>=vintage_age}. Got {guitar.is_vintage(current_year)}")
    print(f"{other.name} is_vintage() - Expected {current_year-1922>=vintage_age}. Got {other.is_vintage(current_year)}")
    print()

    # vintage override test
    current_year = 2025
    print(f"Set year: {current_year}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage(current_year)}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage(current_year)}")


if __name__ == '__main__':
    run_tests()