# -*- coding: utf-8 -*-
"""data dummy libraries.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fpG2LW3SgjSalSdLvRFxaJ_C1C2LvzLF
"""

!pip install Faker
!pip install tabulate

# Import Library
from faker import Faker
from tabulate import tabulate
import random
from datetime import datetime, timedelta
import csv

def show_data(table):

    tab = tabulate(tabular_data = table,
                   headers = table.keys(),
                   tablefmt = "psql",
                   numalign = "center")
    print(tab)

import pandas as pd
from faker import Faker

# Create a Faker instance with Indonesian locale
FAKER = Faker('id_ID')

# Function to generate dummy data for the user table
def generate_name(n):
    return [FAKER.name() for _ in range(n)]

# Function to display the generated table
def show_data(table):
    df = pd.DataFrame(table)
    print(df)

# Function to generate dummy data for the user table
def user_table(n_user, is_print, file_path='tab_user.csv'):
    # Initialize an empty dictionary to store user data
    table = {}

    # Assign user_id sequentially starting from 1
    table["user_id"] = [i + 1 for i in range(n_user)]

    # Generate random names using the Faker library with Indonesian locale
    names = generate_name(n_user)
    # Extract first names and last names
    table['first_name'] = [i.split(' ')[0] for i in names]
    table['last_name'] = [i.split(' ')[1] for i in names]

    # Generate random email addresses based on the generated names
    table['email'] = [f"{name.lower().replace(' ', '')}@{FAKER.free_email_domain()}" for name in names]

    # Generate random phone numbers
    table['phone_number'] = [FAKER.phone_number() for _ in range(n_user)]

    # Convert the dictionary to a DataFrame
    user_df = pd.DataFrame(table)

    # Print the generated table
    if is_print:
        show_data(table)

    # Save the DataFrame to a CSV file
    user_df.to_csv(file_path, index=False)

    return user_df

# Example usage:
# Generate a table of 500 users with Indonesian names, display it, and save it to a CSV file
user_data = user_table(n_user=500, is_print=True, file_path='tab_user.csv')

import pandas as pd
from faker import Faker

fake = Faker()

# Function to generate dummy data for the Library table
def generate_library_data(num_records, is_print=False, file_path='tab_libraries.csv'):
    library_names = [f"Library {chr(65 + i)}" for i in range(num_records)]  # Generate names like "Library A", "Library B", ...
    data = {
        'library_id': range(1, num_records + 1),
        'library_name': library_names
    }
    library_table = pd.DataFrame(data)

    # Print table
    if is_print:
        show_data(library_table)

    # Save DataFrame to CSV
    library_table.to_csv(file_path, index=False)

    return library_table

# Function to display table
def show_data(table):
    print(tabulate(table, headers='keys', tablefmt='fancy_grid'))

# Example usage:
library_data = generate_library_data(num_records=5, is_print=True, file_path='tab_libraries.csv')

import pandas as pd
import random
from faker import Faker
from tabulate import tabulate

fake = Faker()

# Function to generate dummy data for the library_books table
def generate_library_books_data(num_records, num_libraries, num_books):
    data = {
        'lib_book_id': range(1, num_records + 1),
        'library_id': [random.randint(1, num_libraries) for _ in range(num_records)],
        'book_id': list(range(1, num_records + 1))
    }
    return pd.DataFrame(data)

# Function to display table
def show_data(table):
    print(tabulate(table, headers='keys', tablefmt='fancy_grid'))

# Set the number of records you want in your dummy dataset for library_books
num_records_library_books = 500

# Assuming you have 5 libraries (A to E) and 500 books, adjust as needed
num_libraries = 5
num_books = 500

# Generate the library_books table with dummy data
library_books_data = generate_library_books_data(num_records_library_books, num_libraries, num_books)

# Display the generated library_books table using tabulate
show_data(library_books_data)

# Save the library_books_data DataFrame to a CSV file
library_books_data.to_csv('tab_book_library.csv', index=False)

import random
import pandas as pd
from tabulate import tabulate

# Function to display table
def show_data(table):
    print(tabulate(table, headers='keys', tablefmt='fancy_grid'))

def genres_table(n_genres, is_print):
    # List of genres
    generate_genres = ['Fantasy', 'History', 'Thriller', 'Science Fiction', 'Biography', 'Romance', 'Mystery', 'Adventure']

    # Ensure n_genres does not exceed the length of generate_genres
    n_genres = min(n_genres, len(generate_genres))

    # Create a table
    table = {}
    table["genre_id"] = [i+1 for i in range(n_genres)]
    table['genre_name'] = random.sample(generate_genres, n_genres)

    # Print table
    if is_print:
        show_data(table)

    return table

# Set the number of genres you want in your dummy dataset
num_genres = 8

# Generate the genres table with dummy data
genres_data = genres_table(n_genres=num_genres, is_print=True)

# Save DataFrame to CSV with the desired file name
pd.DataFrame(genres_data).to_csv('tab_genres.csv', index=False)

import random
import pandas as pd

def books_table(n_books, is_print, file_path='goodreads_data.csv', csv_filename='tab_book.csv'):
    # Read data from CSV into a DataFrame
    df = pd.read_csv(file_path, encoding='utf-8')

    # Remove whitespaces from column names
    df.columns = df.columns.str.strip()

    # Get unique data from the 'Author' and 'Book' columns in the DataFrame
    unique_authors = df['Author'].unique()
    unique_books = df['Book'].dropna().unique()

    # Ensure that n_books does not exceed the length of unique_books
    n_books = min(n_books, len(unique_books))

    # Create a table dictionary
    table = {}
    # Assign sequential book_id starting from 1
    table['book_id'] = list(range(1, n_books + 1))

    # Select titles and authors simultaneously from unique data
    selected_books_authors = random.sample(list(zip(unique_books, unique_authors)), n_books)
    table['title'], table['author'] = zip(*selected_books_authors)

    # Generate random genre_id and quantity for each book
    table['genre_id'] = [random.randint(1, 8) for _ in range(n_books)]
    table['quantity'] = [random.randint(1, 5) for _ in range(n_books)]

    # Print the table
    if is_print:
        show_data(table)

    # Save DataFrame to CSV with the desired file name
    pd.DataFrame(table).to_csv(csv_filename, index=False)

    print(f"Data has been saved to '{csv_filename}'")

    return table

# Additional function to display data
def show_data(data):
    df = pd.DataFrame(data)
    print(df)

# Example usage:
# Generate a table of 500 books, display it, and save it to a CSV file
books_data = books_table(n_books=500, is_print=True, file_path='goodreads_data.csv', csv_filename='tab_book.csv')

import random
from faker import Faker
from datetime import timedelta
import pandas as pd

fake = Faker()

def loan_table(n_loans, is_print, file_path='tab_loan.csv'):
    loan_data = []
    user_loan_count = {}

    def can_loan_more_books(user_id):
        return user_loan_count.get(user_id, 0) < 2

    for i in range(n_loans):
        user_id = random.randint(1, 500)
        book_id = random.randint(1, 500)

        if can_loan_more_books(user_id):
            loan_status = random.choice(['On Loan', 'Returned', 'Overdue'])

            user_loan_count[user_id] = user_loan_count.get(user_id, 0) + 1

            loan_data.append({
                'loan_id': i + 1,
                'user_id': user_id,
                'book_id': book_id,
                'loan_date': fake.date_time_between(start_date='-30d', end_date='now', tzinfo=None).date(),
                'due_date': None,
                'return_date': None,
                'loan_status': loan_status,
            })

    # Calculate due_date as 14 days from loan_date
    for entry in loan_data:
        entry['due_date'] = entry['loan_date'] + timedelta(days=14)

    # Calculate return_date based on loan status
    for entry in loan_data:
        if entry['loan_status'] in ['Returned', 'Overdue']:
            entry['return_date'] = fake.date_time_between(start_date=entry['loan_date'], end_date='now', tzinfo=None).date()

    # Convert to DataFrame
    loan_df = pd.DataFrame(loan_data)

    # Save DataFrame to CSV
    loan_df.to_csv(file_path, index=False)

    # Print generated data for verification
    if is_print:
        print(loan_df)

    return loan_df

# Example usage:
loan_data = loan_table(300, is_print=True, file_path='tab_loan.csv')

import random
from faker import Faker
from datetime import timedelta
import pandas as pd

fake = Faker()

def hold_table(n_entries, is_print, file_path='tab_hold.csv'):

    hold_data = []
    user_holds_count = {}

    def can_place_hold(user_id):
        return user_holds_count.get(user_id, 0) < 2

    for i in range(n_entries):
        user_id = random.randint(1, 500)
        book_id = random.randint(1, 500)

        if can_place_hold(user_id):
            user_holds_count[user_id] = user_holds_count.get(user_id, 0) + 1

            hold_data.append({
                'hold_id': i + 1,
                'user_id': user_id,
                'book_id': book_id,
                'hold_date': fake.date_time_between(start_date='-30d', end_date='now', tzinfo=None).date(),
                'release_date': fake.date_time_between(start_date='now', end_date='+7d', tzinfo=None).date(),
                'status': 'In Queue'
            })

    # Convert to DataFrame
    hold_df = pd.DataFrame(hold_data)

    # Save DataFrame to CSV
    hold_df.to_csv(file_path, index=False)

    # Print generated data for verification
    if is_print:
        print(hold_df)

    return hold_df

# Example usage:
hold_data = hold_table(50, is_print=True, file_path='tab_hold.csv')
