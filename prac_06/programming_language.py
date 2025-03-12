class ProgrammingLanguage:
    """Stores information about a programming language"""

    def __init__(self, name, typing, reflection, year):
        """Construct programming language object"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of a programming language object"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamically typed"""
        return self.typing == "Dynamic"
