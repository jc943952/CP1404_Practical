"""
Estimate: 20 minutes
Start time: 3:45 PM
Actual time: (record when finished)

This module defines the ProgrammingLanguage class, which stores basic information
about a programming language, such as typing style, reflection support, and year of creation.
"""


class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing.lower() == "dynamic"

    def __str__(self):
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"First appeared in {self.year}")
