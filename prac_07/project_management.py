import datetime
FILENAME = 'projects.txt'
MENU = """
(L)oad project file
(S)ave project file
(D)isplay project 
(F)ilter project
(A)dd new project
(U)pdate project
(Q)uit
"""
print(MENU)

date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
print(f"That day is/was {date.strftime('%A')}")
print(date.strftime("%d/%m/%Y"))

def main():
    choice = input("what ya wanna do")
    while choice != "Q":
        if choice == "L":
        if choice == "S":
        if choice == "D":
        if choice == "F":
        if choice == "U":
        else:
            print('invalid choice')
        print(MENU)
        choice = input("what ya wanna do")
    print("Thank You")

class project:


def load_projects(filename=FILENAME):
    projects = []
    try:
        with open(filename, 'r') as file:
            next(file)  # skip header
            for line in file:
                name, start, priority, cost, completion = line.strip().split('\t')
                projects.append(project(name, start, priority, cost, completion))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return projects

def add_project():
    print("Let's add a new project")
    name = input("Name: ").strip()
    start = input(f"Start date (dd/mm/yyyy): ").strip()
    priority = input("Priority: ").strip()
    cost = input("Cost estimate: ").strip()
    completion = input("Percent complete: ").strip()

    try:
        projects.append(Project(
            name,
            start,
            int(priority),
            float(cost.replace('$', '')),
            int(completion)
        ))
        print(f"Added project: {name}")
    except ValueError:
        print("Invalid input. Project not added.")

if __main__ == "__main__":
    main()