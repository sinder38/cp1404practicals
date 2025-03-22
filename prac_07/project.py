"""
Project
Estimate: 50 minutes
Actual:    minutes
"""

from datetime import datetime



class Project:
    """Stores information about a project"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage, ):
        """Construct a Guitar class instance"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of a Project class"""
        return (
            f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")},"
            f" priority {self.priority},"
            f" estimate: ${self.cost_estimate:,.2f},"
            f" completion: {self.completion_percentage}%")

    # def create_from_input():
    #     """Create a new Project instance from user input"""


def get_name(prompt):
    """Gets a name from the user"""
    name = input(prompt).strip().title()
    while name == "":
        print("Input cannot be blank.")
        name = input(prompt).strip().title()

    return name


def get_date(prompt=""):
    """Gets a valid date from the user"""
    while True:
        try:
            date_string = input(f"{prompt} (d/m/yyyy): ").strip()
            return datetime.strptime(date_string, "%d/%m/%Y").date()
        except ValueError:
            print("Invalid input; enter a valid date in the format d/m/yyyy")


def get_number(prompt="", min_value=0, ):
    """Gets valid number from the user, minimum accepted can be adjusted"""
    while True:
        try:
            value = int(input(prompt).strip())
            if value <= min_value:
                print(f"Number must be > {min_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input; enter a valid number.")
