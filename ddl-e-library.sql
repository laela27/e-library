CREATE TABLE libraries (
    library_id SERIAL PRIMARY KEY,
    library_name VARCHAR(255) NOT NULL
);

CREATE TABLE genres (
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(50) NOT NULL
);

CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre_id INT,
    quantity INT NOT NULL CHECK (quantity >= 0),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);

CREATE TABLE library_books (
    lib_book_id INT PRIMARY KEY,
    library_id INT,
    book_id INT,
    FOREIGN KEY (library_id) REFERENCES libraries(library_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(50),
    phone_number VARCHAR(50)
);

CREATE TABLE loan (
    loan_id INT PRIMARY KEY,
    user_id INT,
    book_id INT,
    loan_date DATE,
    due_date DATE,
    return_date DATE,
    loan_status VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    CONSTRAINT loan_check CHECK (loan_date < due_date)
);

CREATE TABLE hold (
    hold_id INT PRIMARY KEY,
    user_id INT,
    book_id INT,
    hold_date DATE,
    release_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

COPY libraries
FROM 'D:\tab_libraries.csv' 
DELIMITER ',' CSV HEADER;

COPY genres
FROM 'D:\tab_genres.csv' 
DELIMITER ',' CSV HEADER;

COPY books
FROM 'D:\tab_book.csv' 
DELIMITER ',' CSV HEADER;

COPY users
FROM 'D:\tab_user.csv' 
DELIMITER ',' CSV HEADER;

COPY loan
FROM 'D:\tab_loan.csv' 
DELIMITER ',' CSV HEADER;

COPY hold
FROM 'D:\tab_hold.csv' 
DELIMITER ',' CSV HEADER;

COPY library_books
FROM 'D:\tab_book_library.csv' 
DELIMITER ',' CSV HEADER;

SELECT * FROM libraries;
SELECT * FROM genres;
SELECT * FROM books;
SELECT * FROM library_books;
SELECT * FROM users;
SELECT * FROM loan;
SELECT * FROM hold;

--1.Determine the most popular genre based on the number of loans.
SELECT genres.genre_name, COUNT(loan.loan_id) AS total_loans
FROM genres
LEFT JOIN books ON genres.genre_id = books.genre_id
LEFT JOIN loan ON books.book_id = loan.book_id
GROUP BY genres.genre_name
ORDER BY total_loans DESC;

--2.Titles of books that have been borrowed the most based on previous loan data (top 5)?
SELECT books.title, COUNT(loan.loan_id) AS total_loans
FROM books
LEFT JOIN loan ON books.book_id = loan.book_id
GROUP BY books.title
ORDER BY total_loans DESC
LIMIT 5;

--3 .Which books currently have the highest number of hold requests based on the hold queue data?


SELECT b.book_id, b.title, g.genre_name, COUNT(h.book_id) AS hold_count
FROM books b
JOIN genres g ON b.genre_id = g.genre_id
JOIN hold h ON b.book_id = h.book_id
GROUP BY b.book_id, b.title, g.genre_name
ORDER BY hold_count DESC
LIMIT 5;

---4.How many users are still in the queue for book holds in December based on the hold queue data?
SELECT COUNT(DISTINCT user_id) AS users_in_queue
FROM hold
WHERE EXTRACT(MONTH FROM hold_date) = 12;

--5 Which libraries have the highest circulation based on recent loan data?
SELECT l.library_id, l.library_name, COUNT(lo.loan_id) AS circulation_count
FROM libraries l
LEFT JOIN library_books lb ON l.library_id = lb.library_id
LEFT JOIN loan lo ON lb.book_id = lo.book_id
GROUP BY l.library_id, l.library_name
ORDER BY circulation_count DESC
LIMIT 5;




