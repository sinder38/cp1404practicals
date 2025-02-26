"""
CP1404/CP5632 Practical
Hex Colours program
"""

COLOUR_NAME_TO_HEX = {
    "absolute zero": "#0048ba",
    "acid green": "#b0bf1a",
    "alice blue": "#f0f8ff",
    "alizarin crimson": "#e32636",
    "amaranth": "#e52b50",
    "amber": "#ffbf00",
    "amethyst": "#9966cc",
    "antique white": "#faebd7",
    "apricot": "#fbceb1",
    "aqua": "#00ffff"
}


def main():
    """Program to match colour name with its hex code"""
    name = input("Enter hex colour name: ").strip().lower()
    try:
        print(COLOUR_NAME_TO_HEX[name])
    except KeyError:
        print("Unknown colour name")


if __name__ == "__main__":
    main()
