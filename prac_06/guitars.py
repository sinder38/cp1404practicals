"""
CP1404/CP5632 Practical
Guitar playing
"""
from prac_06.guitar import Guitar


def main():
    """Guitar playground program"""
    guitars = []

    print("My guitars!")
    get_guitar_details(guitars)

    if guitars:
        biggest_name_length = max([len(guitar.name) for guitar in guitars]) #NOTE: good enough, but could be better
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>{biggest_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars :( Quick, go and buy one!")


def get_guitar_details(guitars):
    """Gets guitar details from user input"""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")

        name = input("Name: ")

if __name__ == "__main__":
    main()
