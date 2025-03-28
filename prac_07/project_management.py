from project import Project
from datetime import datetime

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

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
ROW_SEPARATOR = "\n"

# Display config
STARTING_INDEX = 0
PADDING_STRING = "  "

# Input config
CONFIRM_INPUTS = ("y", "")  # only lowercase


def main():
    """Project manager program main function"""
    # Init
    print("Welcome to Pythonic Project Management")
    projects, projects_len = load_projects()

    # Main cycle
    print(MENU)
    choice = input(CHOICE_PROMPT).strip().upper()
    while choice != "Q":
        if choice == "L":
            projects, projects_len = load_projects()
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            display_filtered_projects(projects)
        elif choice == "A":
            print("Let's add a new project")
            insert_into_sorted(projects, Project.create_from_input())
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")

        print(MENU)
        choice = input(CHOICE_PROMPT).strip().upper()

    # # Farewell
    if confirm_action("Would you like to save to projects.txt? "):
        save_projects(projects)
    print("Thank you for using custom-built project management software.")


def update_project(projects):
    """Update project progress and priority, enter empty field to retain values"""

    for index, project in enumerate(projects, STARTING_INDEX):
        print(index, project)

    project_index = int(input("Project choice: ")) - STARTING_INDEX

    print(projects[project_index])

    # Update progress
    new_progress = Project.get_completion_from_input("New Percentage: ", skip_capability=True)
    if new_progress:
        projects[project_index].update_progress(new_progress)

    # Update priority
    new_priority = Project.get_priority_from_input("New Priority: ", skip_capability=True)
    if new_priority:  # Check if the input is not empty
        projects[project_index].update_priority(new_priority)

    print("Project updated successfully!")


def insert_into_sorted(items, new_item, key=lambda x: x):
    """Inserts an item into a sorted list while maintaining the order specified by key"""

    i = 0
    while i < len(items):
        if key(new_item) < key(items[i]):
            items.insert(i, new_item)
            return
        i += 1
        # Otherwise, insert at the end
    items.append(new_item)


def display_filtered_projects(projects):
    """Display projects filtered by start date and sorted by start date"""
    filter_date = Project.get_project_date_from_input("Show projects that start after date")
    processed_projects = sorted(filter(lambda p: p.start_date >= filter_date, projects), key=lambda p: p.start_date)

    for project in processed_projects:
        print(project)


def display_projects(projects):
    """Function to display projects in a nice format"""
    incomplete_projects = []
    complete_projects = []
    # Projects are already sorted
    for project in projects:
        if project.is_complete():
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(PADDING_STRING, project)

    print("Complete projects:")
    for project in complete_projects:
        print(PADDING_STRING, project)


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

    projects_len = len(projects)
    print(f"Loaded {projects_len} projects from {DEFAULT_FILENAME}")
    return sorted(projects), projects_len


def save_projects(projects, filename=DEFAULT_FILENAME):
    """Save project data to a txt file in the same format as it was loaded"""
    try:
        with open(filename, mode="w", encoding=TXT_ENCODING) as file:
            # Add table header
            header = COLUMN_SEPARATOR.join([NAME, START_DATE, PRIORITY, COST_ESTIMATE, COMPLETION_PERCENTAGE])
            file.write(header + ROW_SEPARATOR)

            # Add all projects
            for project in projects:
                row = COLUMN_SEPARATOR.join([
                    project.name,
                    project.start_date.strftime("%d/%m/%Y"),
                    str(project.priority),
                    str(project.cost_estimate),
                    str(project.completion_percentage)
                ])
                file.write(row + ROW_SEPARATOR)
    except Exception as e:
        print(f"Opsy, an error occurred while saving the file: {e}")

    projects_len = len(projects)
    print(f"Saved {projects_len} projects to {DEFAULT_FILENAME}")


def confirm_action(prompt=""):
    """Prompts user to confirm their action"""
    confirm = input(f"{prompt}")
    return confirm.lower() in CONFIRM_INPUTS


if __name__ == "__main__":
    main()
