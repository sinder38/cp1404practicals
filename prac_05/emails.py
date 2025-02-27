"""
Emails
Estimate: 10 minutes
Actual:   11 minutes
"""


def main():
    email_to_name = {}
    email = input("Enter your email: ")
    while email != "":
        names = email.split("@").pop(0).split(".")
        print(f"{names}")
        formatted_name = " ".join([n.title() for n in names])
        confirm = input(f"Is your name {formatted_name}? (Y/n) : ")
        if confirm.lower() not in ["y", ""]:
            formatted_name = input("Name: ")
        email_to_name[email] = formatted_name
        email = input("Enter your email: ")

    for email, formatted_name in email_to_name.items():
        print(f"{formatted_name} ({email})")


if __name__ == "__main__":
    main()
