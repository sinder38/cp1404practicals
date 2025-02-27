"""
Word Occurrences
Estimate: 10  minutes
Actual:   8.3 minutes
"""


def main():
    string = input("Text: ")
    lst_str = string.split(" ")
    result = {}
    biggest_len = 0
    for word in lst_str:
        result[word] = result.get(word, 0) + 1
        biggest_len = max(biggest_len, len(word))

    for (word, occurences) in sorted(result.items(), key=lambda x: x[0]):
        print(f"{word:{biggest_len}} : {occurences}")


if __name__ == '__main__':
    main()
