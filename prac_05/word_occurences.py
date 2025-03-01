"""
Word Occurrences
Estimate: 10  minutes
Actual:   8.3 minutes
"""

#WARN: The suggested solution is not great because biggest length can be determined in the first as done
# in my program. Also, no main function.

def main():
    """Program that counts occurrences of words in text string"""
    lst_str = input("Text: ").split(" ")
    result = {}
    biggest_len = 0
    for word in lst_str:
        result[word] = result.get(word, 0) + 1
        biggest_len = max(biggest_len, len(word))

    for (word, occurrences) in sorted(result.items(), key=lambda x: x[0]):
        print(f"{word:{biggest_len}} : {occurrences}")


if __name__ == '__main__':
    main()
