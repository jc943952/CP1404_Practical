"""
CP1404 Assignment 1 - Books to Read
Name: Joshua Andrew
Date Started:15/10/25
GitHub URL: https://github.com/cp1404-students/a1-books-jc943952.git
"""
import csv

FILENAME = "books.csv"

print("Hello, welcome to my library created by Joshua Andrew ")
MENU = """
(A)dd book
(D)isplay books
(C)omplete book 
(R)eset books
(Q)uit
"""
print(MENU)


def main():
    """
    handles the user input, based on the function
    prompts the user to choose from the menu
    Adding a book
    Displaying all books
    Completing a book
    Resetting all books to unread
    Quitting the program
    """
    choice = input('What would you like to do?').strip().upper() # gets input, removes white space and turns uppercase
    while choice != 'Q':
        if choice == 'D':
            display_books()
        elif choice == 'A':
            add_book()
        elif choice == 'C':
            complete_book()
        elif choice == 'R':
            reset_books()
        else:
            print('Invalid option, please choose again')
        print(MENU)
        choice = input('What would you like to do?').strip().upper()
    print('Thank you for using my library.')


def load_book_file(filename=FILENAME):
    """ loads books from csv file into a list of lists
    returns a list of books: title, author, pages, status
    """
    books = []
    with open(filename, 'r') as in_file: # reads file
        for line in in_file:
            author, title, pages, status = line.strip().split(',')
            books.append([author, title, int(pages), status])

    for book in books:
        book[0], book[1] = book[1], book[0]

    return books


def display_books(filename=FILENAME):
    """ displays books in csv file
    The unread books are marked with a '*' while the marked books
    are unmarked
    """
    books = load_book_file(filename)
    number_of_unread_books = 0

    for i, book in enumerate(books):  # i used to keep track of the number of books
        author, title, pages, status = book
        status = status.strip()
        if status == 'u':
            print('{}. {} created {}. {} pages *'.format(i + 1, author,title, pages))
            number_of_unread_books += 1
        else:
            print('{}. {} created {}. {} pages'.format(i + 1, author, title, pages))
    print('Number of unread books: {}'.format(number_of_unread_books))


def add_book():
    """
    Gets the users input on a specific book that can be added to the csv file
    Asks user for title, author, pages, while the status is automatically set to unread
    """
    choice = input('Do you wish to continue? Y / N:').strip().upper()
    if choice == 'N':
        print('Add book cancelled')
        return
    elif choice == 'Y':
        print('Please enter the following to add a book:')
        title = input('Please enter the book title: ')
        author = input('Please enter the book author: ')
        while True:
            try:
                pages = int(input('Please enter the book pages: '))
                if pages <= 0:
                    print('Please enter a positive integer')
                else:
                    break
            except ValueError:
                print('Please enter a valid integer')
        status = 'u'  # inserting default status as unread

        with open(FILENAME, 'a', newline='') as out_file: # amends file to keep existing file
            writer = csv.writer(out_file)
            writer.writerow([title, author, pages, status])
        print('Added book: {} by {}'.format(title, author))


def complete_book(filename=FILENAME):
    """
    Marks selected book as complete
    saves to csv file
    """
    books = load_book_file(filename)
    print('Please choose a book to complete:')
    display_books(filename)
    while True:
        try:
            book_number = int(input('Please enter the book number: '))
            if book_number < 0 or book_number > len(books):
                print('Please enter a valid number :1 - {}'.format(len(books)))
            else:
                if books[book_number - 1][3] == 'c':
                    print('You have already completed this book')
                else:
                    books[book_number - 1][3] = 'c'
                    print('{} has been completed'.format(books[book_number - 1]))
                break
        except ValueError:
            print('Please enter a valid book number {}'.format(len(books)))
    save_file(books)


def reset_books(filename=FILENAME):
    """
    Resets the status of all books in the csv file to 'u'
    saves to csv file
    """
    books = load_book_file(filename)
    for book in books:
        book[3] = 'u'
    save_file(books)
    print('All books have been reset.')


def save_file(books):
    """
    saves the list back to the csv file
    """
    with open(FILENAME, 'w', newline='') as out_file: #overides file updating the existing data
        writer = csv.writer(out_file)
        writer.writerows(books)


if __name__ == '__main__':
    main()
