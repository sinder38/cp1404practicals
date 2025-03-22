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

# Display config
STARTING_INDEX = 1


def main():
    """My Guitars program"""
    print("My guitars!\n")
    guitars = load_guitars()
    display_guitars(guitars)


def load_guitars(filename=DEFAULT_FILENAME):
    """Load guitar data from the file while skipping invalid data"""
    guitars = []
    with open(filename, "r", encoding=CSV_FILE_ENCODING, newline="") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            if len(row) < 3:  # Required count of fields
                continue
            try:
                guitars.append(
                    Guitar(row[GUITAR_NAME_INDEX], int(row[GUITAR_YEAR_INDEX]), float(row[GUITAR_YEAR_INDEX])))
            except ValueError:
                print(f"Skipping invalid row: {row}")

    return guitars


def display_guitars(guitars):
    """Print list of guitars with nice formatting"""
    biggest_name_length = max([len(guitar.name) for guitar in guitars])
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, STARTING_INDEX):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(
            f"Guitar {i}: {guitar.name:>{biggest_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()
