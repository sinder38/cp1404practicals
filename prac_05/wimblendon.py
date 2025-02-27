"""
Wimbledon
Estimate: 15  minutes
Actual:   17 minutes
"""

COUNTRY_COLUMN_INDEX = 1
CHAMPION_COLUMN_INDEX = 2


def main():
    champion_data = load_champion_data("wimbledon.csv")
    champion_to_count, countries = process_champion_data(champion_data)
    display_results(champion_to_count, countries)


def load_champion_data(filename):
    # Columns: Year,Country,Champion,Country,Runner-up,Score in the final
    champion_data = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        file.readline()  # Remove column names

        for line in file:
            row_data = line.strip().split(",")
            champion_data.append((row_data[COUNTRY_COLUMN_INDEX], row_data[CHAMPION_COLUMN_INDEX]))
    return champion_data


def process_champion_data(data):
    champion_to_win_count = {}
    countries = set()
    for row in data:
        country_name = row[0]
        countries.add(country_name)
        champion_to_win_count[row[1]] = champion_to_win_count.get(row[1], 0) + 1

    return champion_to_win_count, countries


def display_results(champion_to_win_count, countries):
    print("Wimbledon Champions: ")

    for name, wins in champion_to_win_count.items():
        print(name, wins)

    print()
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


if __name__ == "__main__":
    main()
