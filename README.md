
# Levo Note API

Levo Note API is a backend service built with Flask that powers the Levo Note client application. This API handles all operations related to note management, including creating, editing, deleting notes, and scheduling reminders.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

Levo Note API includes the following features:

- **Create a Note**: Allows users to create a new note with a title and description.
- **Get All Notes**: Fetches a list of all notes, with support for pagination and search filtering.
- **Get a Note**: Fetches a specific note by ID.
- **Update a Note**: Updates the title and description of a selected note.
- **Delete a Note**: Deletes a specific note.
- **Set Reminder**: Schedules an email reminder for a selected note.
- **Get Reminder**: Retrieves the scheduled reminders for a note.
- **Update Reminder**: Updates the details of a scheduled reminder.
- **Email Scheduling**: Sends reminder emails to specified addresses using APScheduler.

## Technologies Used

This project uses the following technologies and packages:

- **Flask**: A lightweight WSGI web application framework for Python.
- **Flask-SQLAlchemy**: ORM for managing database interactions with PostgreSQL.
- **Flask-Migrate**: Database migration tool for SQLAlchemy.
- **Flask-Mail**: For sending email notifications.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library.
- **PostgreSQL**: Relational database management system used for data storage.
- **APScheduler**: Scheduler for running background tasks, such as sending email reminders.

## Installation

To install the dependencies, create a virtual environment and run:

```bash
pip install -r requirements.txt
```

### Database Setup

1. **Create a PostgreSQL database** for the application.
2. Update the database configuration in the application’s settings (e.g., `config.py`).
3. Run the database migrations:

```bash
flask db upgrade
```

## Usage

To start the Flask API, run:

```bash
flask run
```

The API will be accessible at `http://127.0.0.1:5000`.

## API Endpoints

### Notes

- **GET /api/notes**: Fetch all notes.
- **GET /api/notes/<id>**: Fetch a specific note by ID.
- **POST /api/notes**: Create a new note.
- **PUT /api/notes/<id>**: Update a specific note by ID.
- **DELETE /api/notes/<id>**: Delete a specific note by ID.

### Reminders

- **GET /api/reminders**: Get all reminders.
- **POST /api/reminders**: Set a reminder for a specific note.
- **PUT /api/reminders/<id>**: Update a specific reminder by ID.
- **DELETE /api/reminders/<id>**: Delete a specific reminder by ID.


## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
```
