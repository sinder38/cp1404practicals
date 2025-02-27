"""
Emails
Estimate: 10 minutes
Actual:   11 minutes
"""

CONFIRM_INPUTS = ("y", "")


def main():
    """Program to display emails"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":

        # Extract user's name from the email
        names = email.split("@").pop(0).split(".")
        formatted_name = " ".join(names).title()

        # Confirm automatically extracted name
        confirm = input(f"Is your name {formatted_name}? (Y/n) ")
        if confirm.lower() not in CONFIRM_INPUTS:
            formatted_name = input("Name: ")

        email_to_name[email] = formatted_name

        email = input("Enter your email: ")

    print()
    print_email_data(email_to_name)


def print_email_data(email_to_name):
    """Print all email to name in a pretty way """
    for email, formatted_name in email_to_name.items():
        print(f"{formatted_name} ({email})")


if __name__ == "__main__":
    main()
