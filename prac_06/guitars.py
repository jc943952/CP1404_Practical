"""
Estimate: 60 minutes
Start time: 5:10 PM
Actual time:

Program to store and display a collection of guitars entered by the user.
Demonstrates object lists, input handling, and string formatting.
"""

from guitar import Guitar


def main():
    """Collect and display information about guitars."""
    guitars = []
    print("My guitars!")

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        name = input("Name: ")

    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i, guitar, vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")
main()