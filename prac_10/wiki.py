import wikipedia


def main():
    """Print details of a wikipedia article from user prompt"""
    while True:

        user_input = input("Enter page title: ").strip()
        if user_input == "":
            print("Thank you.")
            break

        display_page_from_prompt(user_input)


def display_page_from_prompt(user_input):
    """Display a wikipedia article from user prompt"""
    try:
        page = wikipedia.page(user_input, auto_suggest=False)

        print(f"\n{page.title}")
        print(f"{page.summary}")
        print(f"URL: {page.url}")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"We need a more specific title. Try one of the following, or a new search:")
        print(e.options)
    except wikipedia.exceptions.PageError:
        print(f"Page id \"{user_input}\" does not match any pages. Try another id!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
