from project import Project
from datetime import datetime

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""

CHOICE_PROMPT = ">>> "

# Save and Load config
TXT_ENCODING = "utf-8"
DEFAULT_FILENAME = "projects.txt"
NAME = "Name"
START_DATE = "Start Date"
PRIORITY = "Priority"
COST_ESTIMATE = "Cost Estimate"
COMPLETION_PERCENTAGE = "Completion Percentage"
COLUMN_SEPARATOR = "\t"

# Display config
STARTING_INDEX = 1

# Input config
CONFIRM_INPUTS = ("y", "")  # only lowercase


def main():
    """Song learner program main function"""
    # Init
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    projects_len = len(projects)
    # sort_songs(songs)
    # songs_length = len(songs)

    print(f"Loaded {projects_len} projects from {DEFAULT_FILENAME}")

    # Main cycle
    print(MENU)
    choice = input(CHOICE_PROMPT).strip().upper()
    while choice != "Q":
        if choice == "D":
            pass
        elif choice == "A":
            pass
        elif choice == "C":
            pass
        else:
            print("Invalid menu choice")

        print(MENU)
        choice = input(CHOICE_PROMPT).strip().upper()

    # # Farewell
    print("Thank you for using custom-built project management software.")


def load_projects(filename=DEFAULT_FILENAME):
    """Load project data from the txt file while skipping invalid data."""
    projects = []

    try:
        with open(filename, mode="r", encoding=TXT_ENCODING) as file:
            # Read the headers
            header = file.readline().strip()
            if not header:
                print("Error: File is empty or header is missing.")
                return projects
            columns = header.split(COLUMN_SEPARATOR)

            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty line

                values = line.split(COLUMN_SEPARATOR)
                if len(values) != len(columns):
                    print(f"Skipping invalid row (incorrect number of columns): {line}")
                    continue

                try:
                    # match column list and row values for ez serialization
                    row = dict(zip(columns, values))

                    project = Project(
                        name=row[NAME].strip(),
                        start_date=datetime.strptime(row[START_DATE].strip(), "%d/%m/%Y").date(),
                        priority=int(row[PRIORITY].strip()),
                        cost_estimate=float(row[COST_ESTIMATE].strip()),
                        completion_percentage=int(row[COMPLETION_PERCENTAGE].strip())
                    )
                    projects.append(project)
                except (ValueError, KeyError):
                    print(f"Skipping invalid row: {line}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    return projects


def confirm_action(prompt=""):
    """Prompts user to confirm their action"""
    confirm = input(f"{prompt} (Y/n): ")
    return confirm.lower() in CONFIRM_INPUTS


if __name__ == "__main__":
    main()
