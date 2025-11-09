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

date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
print(f"That day is/was {date.strftime('%A')}")
print(date.strftime("%d/%m/%Y"))

def main():

def load_projects():

save

if __main__ == "__main__":
    main()