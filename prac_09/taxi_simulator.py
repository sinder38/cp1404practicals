"""
CP1404/CP5632 Practical
Taxi simulator
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
CHOICE_PROMPT = ">>> "


def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_cost = 0.0
    print("Let's drive!")
    print(MENU)
    menu_choice = input(CHOICE_PROMPT).lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            # NOTE: range checking is done outside because of sample output reqs
            taxi_choice = get_number("Choose taxi: ")
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = get_number("Drive how far? ", min_value=0, input_type=float)
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_cost += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(MENU)
        menu_choice = input(CHOICE_PROMPT).lower()


# NOTE: This function is from previous practical.
# I don't want to import from previous practicals because I want each practical to be independent of another
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

if __name__ == "__main__":
    main()