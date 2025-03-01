"""
Wimbledon
Estimate: 15  minutes
Actual:   17 minutes
"""

# NOTE: the most readable solution in my opinion would either a class or just no constants with raw indexes

COLUMNS_TO_EXTRACT = (1, 2)  # Country, Champion name
COUNTRY_DATA_INDEX = 0
CHAMPION_DATA_INDEX = 1


def main():
    """Program to display data about wimbledon champions"""
    # Columns: Year,Country,Champion,Country,Runner-up,Score in the final
    champion_data = load_champion_data("wimbledon.csv", columns_to_extract=COLUMNS_TO_EXTRACT)
    champion_to_count, countries = process_champion_data(champion_data)
    display_results(champion_to_count, countries)


def load_champion_data(filename, columns_to_extract=()):
    """Load requested champion data from the file"""
    champion_data = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        file.readline()  # Remove column names

        if len(columns_to_extract):
            for line in file:
                row_data = line.strip().split(",")
                data_element = tuple(row_data[column_index] for column_index in columns_to_extract)
                champion_data.append(data_element)
        else:  # if empty then extract all rows
            for line in file:
                row_data = line.strip().split(",")
                champion_data.append(row_data)

    return champion_data


def process_champion_data(data):
    """Count champion wins and record their countries"""
    champion_to_win_count = {}
    countries = set()
    for row in data:

        country_name = row[COUNTRY_DATA_INDEX]
        countries.add(country_name)

        champion_name = row[CHAMPION_DATA_INDEX]
        champion_to_win_count[champion_name] = champion_to_win_count.get(champion_name, 0) + 1

    return champion_to_win_count, countries


def display_results(champion_to_win_count, countries):
    """Display champion win results"""
    print("Wimbledon Champions: ")

    for name, wins in champion_to_win_count.items():
        print(name, wins)

    print()
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


if __name__ == "__main__":
    main()
