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

    # NOTE: this is just for better organization and task wanted helper functions
    @staticmethod
    def create_from_input():
        """Create a new Project instance from user input"""
        name = Project.get_name("Name: ")
        start_date = Project.get_date("Start Date")
        priority = Project.get_number("Enter priority (1-5): ", 1, 5)
        cost_estimate = Project.get_number("Enter cost estimate: ", input_type=float)
        completion_percentage = float(input("Enter completion percentage: ").strip())

        return Project(name, start_date, priority, cost_estimate, completion_percentage)

    @staticmethod
    def get_name(prompt):
        """Gets a name from the user"""
        name = input(prompt).strip().title()
        while name == "":
            print("Input cannot be blank.")
            name = input(prompt).strip().title()

        return name

    @staticmethod
    def get_date(prompt=""):
        """Gets a valid date from the user"""
        while True:
            try:
                date_string = input(f"{prompt} (d/m/yyyy): ").strip()
                return datetime.strptime(date_string, "%d/%m/%Y").date()
            except ValueError:
                print("Invalid input; enter a valid date in the format d/m/yyyy")

    @staticmethod
    def get_number(prompt="", min_value=None, max_value=None, input_type: type = int):
        """Gets valid number from the user, minimum and maximum accepted can be adjusted"""
        while True:
            try:
                value = input_type(input(prompt).strip())
                if min_value and value <= min_value:
                    print(f"Number must be > {min_value}.")
                elif max_value and value >= max_value:
                    print(f"Number must be < {max_value}.")
                else:
                    return value
            except ValueError:
                print("Invalid input; enter a valid number.")

