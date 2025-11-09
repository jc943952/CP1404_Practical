from datetime import date
FILENAME = 'guitars.csv'

def main():
    guitars = read_guitars('guitars.csv')

    print("All Guitars:")
    for guitar in guitars:
        print(guitar)

    print("\nSorted by Year (oldest to newest):")
    guitars.sort()
    for guitar in guitars:
        print(guitar)

def read_guitars(filename=FILENAME):
    """
    Load guitars from a CSV file into a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as in_file:  # reads file
        for line in in_file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost.strip())))
    return guitars

class Guitar:
    """Represent a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return how old the guitar is in years."""
        current_year = date.today().year
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age() >= 50


    def __lt__(self, other):
        """Define less-than comparison for sorting by year (oldest first)."""
        return self.year < other.year
if __name__ == "__main__":
    main()