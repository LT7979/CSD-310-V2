

DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;


DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS administrator;


CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    store_hours VARCHAR(20)     NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE administrator (
    admin_id        INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    psswd           VARCHAR(75) NOT NULL,
    PRIMARY KEY(admin_id)
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);


INSERT INTO administrator(first_name, last_name, psswd)
    VALUES('Kevin', 'Mitnik', '09a5078c57a41dc91cbe4ec44bcfeecf');

INSERT INTO store(locale, store_hours)
    VALUES('1703 Wallaby Lane, Sprucstone, TX', '9 AM - 5PM: M-F');

INSERT INTO book(book_name, author, details)
    VALUES('If It Bleeds', 'Stephen King', 'Scary Monsters in the Night');

INSERT INTO book(book_name, author, details)
    VALUES('The Institution', 'Stephen King', 'Creepy Institution!');

INSERT INTO book(book_name, author, details)
    VALUES('The 48 Laws Of Power', 'Robert Greene', "Life Is a Power Game!");

INSERT INTO book(book_name, author)
    VALUES('Atomic Habits', 'James Clear');

INSERT INTO book(book_name, author)
    VALUES('How to Win Friends And Influence People', 'Dale Carnegie');

INSERT INTO book(book_name, author)
    VALUES("Charlotee's Web", 'E.B. White');

INSERT INTO book(book_name, author)
    VALUES('The Great Gatsby', 'F. Scott Fitzgerald');

INSERT INTO book(book_name, author)
    VALUES('The Lion, the Witch, and the Wardrobe', 'C.S. Lewis');

INSERT INTO book(book_name, author)
    VALUES('The Catcher and the Rye', 'J.D. Salinger');


INSERT INTO user(first_name, last_name) 
    VALUES('Peter', 'Parker');

INSERT INTO user(first_name, last_name)
    VALUES('Sam', 'Sepiol');

INSERT INTO user(first_name, last_name)
    VALUES('Linus', 'Torvalds');


INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Peter'), 
        (SELECT book_id FROM book WHERE book_name = 'If It Bleeds')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Sam'),
        (SELECT book_id FROM book WHERE book_name = 'The Institution')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Linus'),
        (SELECT book_id FROM book WHERE book_name = 'The 48 Laws Of Power')
    );
