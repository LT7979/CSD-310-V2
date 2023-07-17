import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    add_table = ("CREATE TABLE wishlist (\
                 wishlist_id     INT         NOT NULL    AUTO_INCREMENT, \
                 user_id         INT         NOT NULL, \
                 book_id         INT         NOT NULL, \
                 PRIMARY KEY (wishlist_id), \
                 CONSTRAINT fk_book \
                 FOREIGN KEY (book_id) \
                 REFERENCES book(book_id), \
                 CONSTRAINT fk_user \
                 FOREIGN KEY (user_id) \
                 REFERENCES user(user_Id) \
                 );")

    cursor.execute(add_table)

    db.commit()

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)
