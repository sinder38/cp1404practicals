"""
CP1404/CP5632 Practical
My Guitars
"""

from guitar import Guitar
import csv

# Save config
DEFAULT_FILENAME = "guitars.csv"
CSV_FILE_ENCODING = "utf-8"
GUITAR_NAME_INDEX = 0
GUITAR_YEAR_INDEX = 1
GUITAR_COST_INDEX = 2
GUITAR_DATA_LENGTH = 3

# Display config
STARTING_INDEX = 1

# Input config
CONFIRM_INPUTS = ("y", "")  # only lowercase


def main():
    """My Guitars program"""
    print("My guitars!\n")
    guitars = load_guitars()
    guitars.sort()  # Sorts by age!
    display_guitars(guitars)
    if confirm_action("\nDo you wish to enter new guitars?"):
        guitars.clear()
        get_guitar_details(guitars)

    if confirm_action("\nDo you wish to save your guitars?"):
        save_guitars(guitars)

def load_guitars(filename=DEFAULT_FILENAME):
    """Load guitar data from the file while skipping invalid data"""
    guitars = []
    with open(filename, "r", encoding=CSV_FILE_ENCODING) as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            if len(row) < GUITAR_DATA_LENGTH:
                continue
            try:
                guitars.append(
                    Guitar(row[GUITAR_NAME_INDEX], int(row[GUITAR_YEAR_INDEX]), float(row[GUITAR_COST_INDEX])))
            except ValueError:
                print(f"Skipping invalid row: {row}")

    return guitars


def save_guitars(guitars, filename=DEFAULT_FILENAME):
    """Save guitar data to the csv file"""
    with open(filename, "w", encoding=CSV_FILE_ENCODING) as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            row = [""] * GUITAR_DATA_LENGTH
            row[GUITAR_NAME_INDEX] = guitar.name
            row[GUITAR_YEAR_INDEX] = guitar.year
            row[GUITAR_COST_INDEX] = guitar.cost
            writer.writerow(row)


def display_guitars(guitars):
    """Print list of guitars with nice formatting"""

    biggest_name_length = max([len(guitar.name) for guitar in guitars])
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, STARTING_INDEX):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(
            f"Guitar {i}: {guitar.name:>{biggest_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def get_guitar_details(guitars):
    """Gets guitar details from user input until name input is empty"""
    while True:
        name = input("Enter guitar name (or press Enter to finish): ").strip()
        if not name:
            break  # Exit if the name is empty
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
        except ValueError:
            print("Invalid input. Please enter a valid year and cost.")
            continue

        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added\n")


def confirm_action(prompt=""):
    """Prompts user to confirm their action"""
    confirm = input(f"{prompt} (Y/n): ")
    return confirm.lower() in CONFIRM_INPUTS


if __name__ == "__main__":
    main()
