# Quiz Application

This is a simple Django-based quiz application where users can attempt multiple-choice questions and view their results.

## Features

- Admin panel to manage questions.

- Dynamic question fetching from the database.

- Tracks user's answers, correctness, and total scores.

- Displays detailed results for each question and the final score.

## Requirements

- Python 3.8+

- Django 4.0+

- SQLite (default database for development)

## Setup Instructions

### 1. Clone the Repository
```
$ git clone <repository-url>
$ cd <project-folder>
```
### 2. Create a Virtual Environment

Create a virtual environment to manage dependencies.
```
$ python -m venv venv
$ source venv/bin/activate # On Windows, use `venv\Scripts\activate`
```
### 3. Install Dependencies

Install the required Python packages from the requirements.txt file.
```
$ pip install -r requirements.txt
```
### 4. Setup the Database

Run the following commands to set up the database and load initial data (if any).
```
$ python manage.py makemigrations
$ python manage.py migrate
```
### 5. Create a Superuser

Create an admin user to access the Django admin panel.
```
$ python manage.py createsuperuser
```
Follow the prompts to set up the admin credentials.

### 6. Run the Development Server

Start the Django development server.
```
$ python manage.py runserver
```
Access the application at http://127.0.0.1:8000/.

## Admin Panel

To add questions, log in to the Django admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials created earlier.

- Navigate to the Questions section.

- Add a new question with its text, options (A, B, C, D), and the correct option.

Contact

For any questions or suggestions, contact [liteshgoyal55@gmail.com].
