"""
CP1404/CP5632 Practical
Taxi simulator
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

# Input
MENU = "q)uit, c)hoose taxi, d)rive"
CHOICE_PROMPT = ">>> "

# Display
STARTING_INDEX = 0
COST_PRECISION = 2

# Gameplay
STARTING_COST = 0.0
STARTING_TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    """Taxi driving simulator"""
    current_taxi = None
    taxis = STARTING_TAXIS
    total_cost = STARTING_COST

    # Main Cycle
    print("Let's drive!")
    print(MENU)
    menu_choice = input(CHOICE_PROMPT).lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            # NOTE: range checking is done outside because of sample output reqs
            taxi_choice = get_number("Choose taxi: ") + STARTING_INDEX
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
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.{COST_PRECISION}f}")
                total_cost += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_cost:.{COST_PRECISION}f}")
        print(MENU)
        menu_choice = input(CHOICE_PROMPT).lower()

    # Farewell
    print(f"Total trip cost: ${total_cost:.{COST_PRECISION}f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display taxis in an indexed table"""
    for i, taxi in enumerate(taxis, start=STARTING_INDEX):
        print(f"{i} - {taxi}")


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
