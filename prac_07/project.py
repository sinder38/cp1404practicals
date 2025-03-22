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
            f" estimate: ${self.cost_estimate:.2f},"
            f" completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Return True if this Project is lower priority than the other Project"""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is complete"""
        return self.completion_percentage >= 100

    def update_progress(self, new_completion_percentage):
        self.completion_percentage = new_completion_percentage

    def update_priority(self, new_priority):
        self.priority = new_priority

    # NOTE: this is just for better organization and task wanted helper functions
    @staticmethod
    def create_from_input():
        """Create a new Project instance from user input"""
        name = Project.get_name_from_input()
        start_date = Project.get_project_date_from_input()
        priority = Project.get_priority_from_input()
        cost_estimate = get_number("Enter cost estimate: $", input_type=float)
        completion_percentage = Project.get_completion_from_input()

        return Project(name, start_date, priority, cost_estimate, completion_percentage)

    @staticmethod
    def get_name_from_input(prompt="Name: "):
        """Gets a name from the user"""
        name = input(prompt).strip().title()
        while name == "":
            print("Input cannot be blank.")
            name = input(prompt).strip().title()

        return name

    @staticmethod
    def get_project_date_from_input(prompt="Start Date"):
        """Gets a valid date from the user"""
        while True:
            try:
                date_string = input(f"{prompt} (d/m/yyyy): ").strip()
                return datetime.strptime(date_string, "%d/%m/%Y").date()
            except ValueError:
                print("Invalid input; enter a valid date in the format d/m/yyyy")

    @staticmethod
    def get_priority_from_input(prompt="Priority: ", **kwargs):
        """Gets a priority from the user"""
        return get_number(prompt, 1, **kwargs)

    @staticmethod
    def get_completion_from_input(prompt="Percent complete: ", **kwargs):
        """Gets a priority from the user"""
        return get_number(prompt, 1, max_value=100, **kwargs)


def get_number(prompt="", min_value=None, max_value=None, input_type: type = int, skip_capability=False):
    """Gets valid number from the user, inclusive minimum and maximum accepted can be adjusted.
     Skip capability allows user to skip the prompt by pressing enter, the function will return None"""
    while True:
        try:
            response = input(prompt).strip()

            if skip_capability and response == "":  # Skip and return None
                return None

            value = input_type(response)
            if min_value and value < min_value:
                print(f"Number must be >= {min_value}.")
            elif max_value and value > max_value:
                print(f"Number must be <= {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input; enter a valid number.")
