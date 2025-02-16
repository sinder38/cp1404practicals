"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)


# NOTE: I like this one much more
def get_valid_number(_type=int):
    """get valid number from user of appropriate type"""
    while True: # yes
        user_input = input(f"Enter a valid {_type.__name__}: ")
        try:
            return _type(user_input)
        except ValueError:
            print(f"Invalid input. Please enter a valid {_type.__name__}.")
