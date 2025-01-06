#Notenique - Notes Management Application


Notenique is a user-friendly, feature-rich notes management application designed to help users create, organize, and manage their notes effectively. Whether you're a student, professional, or hobbyist, Notenique provides an intuitive interface to keep your notes secure and accessible.

Features
User Authentication: Secure login and registration system.
Personalized Notes: Users can create, edit, and delete notes.
Note Display: List of notes with titles and excerpts for easy browsing.
Responsive Design: Fully responsive and mobile-friendly interface, powered by Bootstrap 5.
Search Notes: Quickly search and find your notes using the built-in search functionality.
Profile Management: Users can upload and update their profile images.
Secure Storage: Notes are stored securely and are accessible at any time.
Technologies Used
Frontend: HTML, CSS (Bootstrap 5)
Backend: Python (Flask)
Database: SQLite
Authentication: Flask-Login
ORM: SQLAlchemy
Form Handling: WTForms
Installation
Prerequisites
Ensure you have Python 3.x and pip installed. You can download Python from the official Python website.

Steps to Install
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/notenique.git
cd notenique
Create a virtual environment:

bash
Copy code
python3 -m venv venv
Activate the virtual environment:

For Windows:

bash
Copy code
venv\Scripts\activate
For Mac/Linux:

bash
Copy code
source venv/bin/activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database:

bash
Copy code
flask db init
flask db migrate
flask db upgrade
Run the application:

bash
Copy code
flask run
Open the app in your browser:

arduino
Copy code
http://127.0.0.1:5000/
Usage
Login/Signup: Users can sign up or log in to access their personalized notes.
Create Notes: Logged-in users can create new notes from the "Create Notes" page.
Manage Notes: Users can edit or delete notes they have created.
Search: Use the search bar to find notes based on title or content.
Profile: Users can upload their profile image and view their personalized page.
Contributing
We welcome contributions to make Notenique better! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes.
Push your branch to your forked repository.
Open a pull request for review.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Flask: A micro web framework for Python.
Bootstrap 5: A popular framework for responsive web design.
SQLAlchemy: An ORM for database management in Python.
Flask-Login: A Flask extension for user session management.
