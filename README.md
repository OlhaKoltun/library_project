
# My Library - Library Management System

## Introduction

"My Library" is a web application built using Python and the Django framework with a PostgreSQL database. It serves as a Library Management System that enables authorized users and librarians to interact with the book catalog and manage the book rental process.

## Features

### User and Librarian Authentication

-   The project incorporates a robust user authentication system. Users can create accounts, log in, and access their profiles to view available books and rent them for reading.
-   Librarians are also required to authenticate themselves and are granted extended access rights.

### Book Browsing and Rental

-   Authenticated users can browse the library's book catalog, which includes information such as book titles, authors, and the number of available copies. Books available for rental are clearly indicated.
-   Users can select a book and rent it, and the book's status will be updated to "rented," with the number of available copies decreased accordingly.

### Catalog Management by Librarian

-   Librarians have the privilege of adding new books to the catalog, specifying details like the title, author, and the number of available copies. They can also add information about new authors to enrich the catalog.
-   Each book in the catalog has a unique identifier for easy identification and management.

### Book Return Processing

-   When a user finishes reading a rented book, they can initiate the return process, making the book available for rental again.
-   Librarians can view a list of rented books and track their return. They also monitor the planned return dates to prevent delays.

## Technical Details

-   The project is developed using Python, leveraging the Django framework for high performance and extensibility.
-   PostgreSQL is utilized as the database, ensuring robust data storage and efficient database queries.
-   The project's dependencies and environment are managed using `pipenv`.
-   It follows a modular and application-based structure, facilitating maintenance and the addition of new features.

## Installation

1. Ensure that you have Python and PostgreSQL installed on your system.
2. Clone the project repository from GitHub.
3. Install `pipenv` if you haven't already, and activate the virtual environment:
    
    Copy code
    
    `pip install pipenv`

    `pipenv shell` 
    
4. Install project dependencies from the Pipfile:
    
    Copy code
    
    `pipenv install` 
    
   1. Configure the PostgreSQL database and apply migrations:
    
       Copy code
    
   `python manage.py makemigrations` 

    `python manage.py migrate` 
    
6. Start the Django server:
    
    Copy code
    
    `python manage.py runserver` 
    

## Usage

1.  Open a web browser and navigate to `http://localhost:8000/` to access "My Library" - the Library Management System.
2.  If you are a new user, you can create an account to get started. If you are a librarian, log in using your librarian credentials.
3.  Once logged in, users can browse the available books, view book details, and rent books for reading.
4.  Librarians can access additional features, such as adding new books and authors, viewing all books in the catalog, and managing book rentals and returns.

## Contributing

We welcome contributions to improve "My Library." If you find any bugs or have suggestions for new features, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://en.wikipedia.org/wiki/MIT_License). Feel free to use, modify, and distribute it as per the terms of the license.

----------

Thank you for choosing "My Library"! Happy reading and managing your library!
