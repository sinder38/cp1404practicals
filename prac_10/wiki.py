import wikipedia


def main():
    """Print details of a wikipedia article from user prompt"""
    print("Enter a Wikipedia page title or search phrase (blank to quit):")

    while True:
        user_input = input("> ").strip()
        if user_input == "":
            print("Goodbye!")
            break
        try:
            page = wikipedia.page(user_input, auto_suggest=False)

            print(f"\nTitle: {page.title}")
            print(f"URL: {page.url}")
            print(f"Summary:\n{wikipedia.summary()}\n")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
