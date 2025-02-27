"""
CP1404/CP5632 Practical
Hex Colours program
"""

COLOUR_NAME_TO_HEX = {
    "absolutezero": "#0048ba",
    "acidgreen": "#b0bf1a",
    "aliceblue": "#f0f8ff",
    "alizarincrimson": "#e32636",
    "amaranth": "#e52b50",
    "amber": "#ffbf00",
    "amethyst": "#9966cc",
    "antiquewhite": "#faebd7",
    "apricot": "#fbceb1",
    "aqua": "#00ffff"
}


def main():
    """Program to match colour name with its hex code"""
    name = input("Enter hex colour name: ").strip().lower()
    try:
        print(f"Code for {name} is {COLOUR_NAME_TO_HEX[name]}")
    except KeyError:
        print("Unknown colour name")


if __name__ == "__main__":
    main()
