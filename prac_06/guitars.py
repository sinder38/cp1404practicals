"""
CP1404/CP5632 Practical
Guitar playing
"""
from prac_06.guitar import Guitar


def main():
    """Guitar playground program"""
    guitars = []

    print("My guitars!")
    # get_guitar_details(guitars)

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
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
