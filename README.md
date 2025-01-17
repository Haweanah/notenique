# Notenique - Notes Management Application


Notenique is a user-friendly, feature-rich notes management application designed to help users create, organize, and manage their notes effectively. Whether you're a student, professional, or hobbyist, Notenique provides an intuitive interface to keep your notes secure and accessible.

### [Visit the App](https://notenique.onrender.com/) 🚀

## Features
- User Authentication: Secure login and registration system.
- Personalized Notes: Users can create, edit, and delete notes.
- Note Display: List of notes with titles and excerpts for easy browsing.
- Responsive Design: Fully responsive and mobile-friendly interface, powered by       Bootstrap 5.
- Profile Management: Users can upload and update their profile images.
-- Secure Storage: Notes are stored securely and are accessible at any time.

## Technologies Used
- Frontend: HTML, CSS (Bootstrap 5)
- Backend: Python (Flask)
- Database: PostgreSQL (previously SQLite)
- Authentication: Flask-Login
- ORM: SQLAlchemy
- Form Handling: WTForms

## Switching from SQLite to PostgreSQL
To switch from SQLite to PostgreSQL, follow these steps:
1. Install PostgreSQL and create a database:
   - bash
      - sudo -u postgres psql
      - CREATE DATABASE notenique_db

2. Update config.py to point to PostgreSQL:
python
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/notenique_db'

3. Install psycopg2 (PostgreSQL adapter for Python):
pip install psycopg2

4. Reinitialize the database:
flask db init
flask db migrate
flask db upgrade

Deployment on Render
To deploy the application on Render:

Create a new web service on Render.
Connect your GitHub repository and select the branch you want to deploy.
Set the environment variables, including FLASK_APP, FLASK_ENV, and the PostgreSQL database URL.
Configure the build and start commands:
Build command: pip install -r requirements.txt
Start command: flask run
Render will automatically detect the Flask application and deploy it. After deployment, you can access the app via the provided URL.


## Installation
### Prerequisites
Ensure you have Python 3.x and pip installed. You can download Python from the official Python website.

### Steps to Install
- Clone the repository:
git clone https://github.com/haweanah/notenique.git
cd notenique
- Create a virtual environment:
-- bash
python3 -m venv venv
Activate the virtual environment:

- For Windows:
venv\Scripts\activate
--For Mac/Linux:
source venv/bin/activate

- Install the required dependencies:
- bash
pip install -r requirements.txt
- Set up the database:
- bash
flask db init
flask db migrate
flask db upgrade
- Run the application:
- bash
flask run
- Open the app in your browser:
http://127.0.0.1:5000/

## Usage
### Login/Signup:
Users can sign up or log in to access their personalized notes.
### 
Create Notes: 
Logged-in users can create new notes from the "Create Notes" page.
### Manage Notes: 
Users can edit or delete notes they have created.
### Profile:
Users can upload their profile image and view their personalized page.

## Live Demo
<video controls src="Media Player - 17 January 2025.mp4" title="Title"></video>

Experience the app live by clicking the link below:

[Notenique Live](https://notenique.onrender.com/)



## Contributing
We welcome contributions to make Notenique better! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes.
Push your branch to your forked repository.
Open a pull request for review.
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Flask: A micro web framework for Python.
Bootstrap 5: A popular framework for responsive web design.
SQLAlchemy: An ORM for database management in Python.
Flask-Login: A Flask extension for user session management.

### [Notenique](https://notenique.onrender.com/) 🚀

## Author: Hauwa, Abdulkadir
@ahauwa48@yahoo.com
