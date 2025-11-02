"""
Estimate: 20 minutes
Start time: 4:05 PM
Actual time: 4:40pm

This program demonstrates the use of the ProgrammingLanguage class by creating
several examples and displaying their details.
"""

from programming_language import ProgrammingLanguage


def main():
    """Create and display some programming languages."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)
    print(ruby)
    print(visual_basic)

    languages = [python, ruby, visual_basic]
    for language in languages:
        print(language)

    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()