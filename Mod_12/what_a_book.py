""" 
    Title: what_a_book.py
    Author: Samuel Ford
    Date: 24 July 2023
    Description: Book Program for Book lovers alike
    Modified From what_a_book.py By Professor Krasso
"""
#normal import statements for mysql
import sys
import mysql.connector
from mysql.connector import errorcode
import hashlib

#configuration for Database
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#displaying the Menu
def display_menu():
    print("\n  Whatabook Main Menu")

    print("    1. Show available Books\n    2. View Whatabook Locations\n    3. View My Account\n    4. Exit\n    5. Admin Panel")

    try:
        choice = int(input('      <enter a number> '))

        return choice
    except ValueError:
        print("\n  Error! Invalid entry, exiting program...\n")

        sys.exit(0)

def validate_admin(_cursor):

    try:
        #there should only be one admin with ID of 1
        admin_id = (input('\n      <enter an admin ID number> '))

        #error handling
        if admin_id != "1":
            print("\n  Invalid number, exiting...\n")
            sys.exit(0)

        #getting admin password
        admin_pass = input('\n     ---enter admin password:---')

        #encoding password to MD5 Hash
        admin_pass = hashlib.md5(admin_pass.encode())

        #converting encoded hash to hex for database comparison
        admin_pass = (admin_pass.hexdigest())

        #creating Tuple for ID and password
        admin_login = admin_pass

        #getting admin ID and password from admin in the database
        _cursor.execute("SELECT psswd from administrator WHERE admin_id = 1")

        #getting values to compare against
        validate = _cursor.fetchall()

        for i in validate:
        #if the password is wrong, throw an error
            if admin_login != i[0]:
                print(i[0])
                print(admin_login)
                sys.exit(0)

            #if credentials are correct, return admin ID
            if admin_login == i[0]:
                return admin_id


    #value error handling
    except ValueError:
        print("\n  Invalid number, exiting...\n")

        sys.exit(0)

#Admin Menu choices
def show_admin_menu(_cursor):
    try:
        print("\n      <Admin Menu>")
        print("        1. Add New Book\n        2. MAIN MENU ")
        admin_option = int(input('        <Enter a number> '))

        #if choice is out of range, exit
        if admin_option < 0 or admin_option > 2:
            print("\n  Invalid number, exiting...\n")
            sys.exit(0)

        return admin_option

    except ValueError:
        print("\n  Invalid number, exiting...\n")

#add new book with values given for title, author, description
def add_new_book(_cursor, _book_name, _author, _details):
    add_book = """INSERT INTO book(book_name, author, details) VALUES (%s, %s, %s)"""
    _cursor.execute(add_book, (_book_name, _author, _details))
    return _book_name, _author, _details

def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale, store_hours from store")

    locations = _cursor.fetchall()

    print("\n  <Showing Store Locations>")

    #printing location and hours
    for location in locations:
        print("  Locale: {}\n".format(location[1]) + "  Hours: {}\n".format(location[2]))

def validate_user():

    try:
        user_id = int(input('\n      <Enter an id number> '))

        if user_id < 0 or user_id > 3:
            print("\n  Invalid number, exiting...\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Invalid number, exiting...\n")

        sys.exit(0)

def show_books(_cursor):
    # inner join for displaying books 
    _cursor.execute("SELECT book_id, book_name, author, details from book")
 
    books = _cursor.fetchall()

    print("\n  <Displaying All Books> ")
    
    #a loop for parsing out the books and printing them to lines 
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[1], book[2], book[3]))

def show_account_menu():
    """ display the users account menu """

    try:
        print("\n      <account Menu>")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        account_option = int(input('        <Enter a number> '))

        return account_option
    except ValueError:
        print("\n  Invalid number, Exiting...\n")

        sys.exit(0)

def show_wishlist(_cursor, _user_id):
    """ query the database for a list of books added to the users wishlist """

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n        -- DISPLAYING WISHLIST ITEMS --")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):
    """ query the database for a list of books not in the users wishlist """

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n        -- DISPLAYING AVAILABLE BOOKS --")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:

    db = mysql.connector.connect(**config) # connecting to the database 

    cursor = db.cursor()

    print("\n  Welcome to Whatabook! We hope you enjoy it! ")

    user_selection = display_menu() 

    while user_selection != 4:

        # if the user selects option 1, call the show_books method and display the books
        if user_selection == 1:
            show_books(cursor)

        # if the user selects option 2, call the show_locations method and display the configured locations
        if user_selection == 2:
            show_locations(cursor)

        # if the user selects option 3, call the validate_user method to validate the entered user_id 
        # call the show_account_menu() to show the account settings menu
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            # while account option does not equal 3
            while account_option != 3:

                # if the use selects option 1, call the show_wishlist() method to show the current users 
                # configured wishlist items 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # if the user selects option 2, call the show_books_to_add function to show the user 
                # the books not currently configured in the users wishlist
                if account_option == 2:

                    # show the books not currently configured in the users wishlist
                    show_books_to_add(cursor, my_user_id)

                    # get the entered book_id 
                    book_id = int(input("\n        Enter the id of the book you want to add: "))
                    
                    # add the selected book the users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() # commit the changes to the database 

                    print("\n        Book id: " + str(book_id) + " was added to your wishlist!")

                # if the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please retry...")

                # show the account menu 
                account_option = show_account_menu()
        
        #admin panel option: validate admin used for validation
        if user_selection == 5:
            my_admin_login = validate_admin(cursor)
            admin_option = show_admin_menu(cursor)

            while admin_option != 2:

                #asking for new book values
                if admin_option == 1:
                    new_title = input("\n   Enter Book Title: \n")
                    new_author = input("\n   Enter Book Author: \n")
                    new_desc = input("\n   Enter Book description<optional>: \n")
                    add_new_book(cursor, new_title, new_author, new_desc)

                    db.commit()

                    #print new book added
                    print("\n added new book with Title: " + new_title + "\n Author: " + new_author + "\n details: " + new_desc)

                if admin_option < 0 or admin_option > 2:
                    print("\n      Invalid option, please retry...")
 
                admin_option = show_admin_menu(cursor)
        
        # if the user selection is less than 0 or greater than 5, display an invalid user selection
        if user_selection < 0 or user_selection > 5:
            print("\n      Invalid option, please retry...")
            
        # show the main menu
        user_selection = display_menu()

    print("\n\n  Program terminated...")

except mysql.connector.Error as err:
    #error handling 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the MySQL connection """

    db.close()