"""
CP1404/CP5632 Practical
Taxi simulator
"""

from prac_09.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
CHOICE_PROMPT = ">>> "


def main():
    print("Let's drive!")
    print(MENU)
    menu_choice = input(CHOICE_PROMPT).lower()
    while menu_choice != "q":
        if menu_choice == "c":
            pass
        elif menu_choice == "d":
            pass
        else:
            print("Invalid option")
        print(MENU)
        menu_choice = input(CHOICE_PROMPT).lower()


def get_number(prompt="", min_value=None, max_value=None, input_type: type = int, skip_capability=False):
    """Gets valid number from the user, inclusive minimum and maximum accepted can be adjusted.
     Skip capability allows user to skip the prompt by pressing enter, the function will return None"""
    while True:
        try:
            response = input(prompt).strip()

            if skip_capability and response == "":  # Skip and return None
                return None

            value = input_type(response)
            if min_value and value < min_value:
                print(f"Number must be >= {min_value}.")
            elif max_value and value > max_value:
                print(f"Number must be <= {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input; enter a valid number.")
