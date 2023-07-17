INSERT INTO store(locale)
    VALUES('1703 Wallaby Lane, Sprucstone, TX');

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