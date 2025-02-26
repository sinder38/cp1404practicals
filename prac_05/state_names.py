"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}


def main():
    # print states code - name pairs
    for (key, value) in CODE_TO_NAME.items():
        print_code_name_pair(key, value)

    state_code = input("Enter short state: ").upper()
    while state_code != "":
        try:
            print_code_name_pair(state_code, CODE_TO_NAME[state_code])
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()


def print_code_name_pair(pair_key, pair_value):
    print(f"{pair_key:<3} is {pair_value}")


if __name__ == "__main__":
    main()
