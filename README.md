# Student Entry System

A Django-based web application for managing student records with integration of both Django Rest Framework (DRF) for API access and Django templates for a web interface. This project allows administrators to create, update, and delete student records through both a user-friendly web interface and a REST API. It provides different views for managing student records: the Django template views allow for traditional form-based interactions, while the REST API endpoints enable programmatic access and manipulation of student data.

## Features

- **Student Model:** Manages student information including Name, Age, Address, Grade, and Major.
- **Admin Interface:** Record new student details, update existing records, and delete records.
- **Django Templates:** Provides a user-friendly web interface for creating, updating, and deleting student records using form-based interactions.
- **REST API:** Exposes student model via a REST API for CRUD operations.
- **Port Configuration:** Runs on `localhost` at port `8025`.

## Project Setup

### Prerequisites

- Python 3.10 or later
- Pipenv for virtual environment management

### Installation

1. **Clone the Repository:**
   ```sh
   git clone git@github.com:Neerazan/student_entry.git
   cd student_entry
   ```

2. **Set up Virtual Environment:**
   ```sh
   pipenv install
   pipenv shell
   ```

3. **Set Up Environment Variables**

   Copy the sample environment file and configure your settings:

   ```sh
   cp .env-sample .env
   ```

4. **Update `.env` with your database and other settings. Example `.env`** configuration:

   ```env
   DEBUG = True
   SECRET_KEY = '<your-secret-key>'
   #  Need to setup only if Debug is False 
   DATABASE_PASSWORD = '<your-database-password>'
   DATABASE_USER = '<your-database-user>'
   DATABASE_NAME = '<your-database-name>'
   DATABASE_HOST = '<your-database-host>'
   DATABASE_PORT = '<your-database-port>'
   ```

5. **Run Migrations**

   ```sh
   make migrate
   ```

6. **Create Superuser (Optional)**

   ```sh
   make superuser
   ```

7. **Run the Development Server**

   ```sh
   make run
   ```

The application will be available at http://localhost:8025.


## Code Quality

### Linting

Run linting checks using:

   ```sh
   make lint
   ```

### Pre-commit Hooks

   Install pre-commit hooks to ensure code quality:

   ```sh
   make install-pre-commit
   ```

## Makefile Targets

   * **install:** Install project dependencies.
   * **install-pre-commit:** Install pre-commit hooks.
   * **lint:** Run linting checks.
   * **run:** Start the Django development server on port 8025.
   * **migrate:** Apply database migrations.
   * **migrations:** Create new migrations.
   * **shell:** Open Django shell.
   * **superuser:** Create a Django superuser.
   * **update:** Install dependencies and apply migrations.
   * **app:** Create a new Django app (requires `name` variable).

## Usage

### Admin Interface

1. Access the admin interface at `http://localhost:8025/admin/`
2. Log in using the superuser credentials created earlier
3. Navigate to the Students section to manage student records

### REST API

The REST API endpoints are available at:

- List/Create: `http://localhost:8025/api/students/`
- Retrieve/Update/Delete: `http://localhost:8025/api/students/<slug>/`

### DJANGO TEMPLATE
- List/Create: `http://localhost:8025/students-template/`
- Retrieve/Update/Delete: `http://localhost:8025/api/students/<slug>/`

Use appropriate HTTP methods (GET, POST, PUT, DELETE) to interact with the API.

## API Documentation

For detailed API documentation, visit `http://localhost:8025/api/docs/` after starting the development server.


## License

Distributed under the MIT License. See `LICENSE` file for more information.

## Contact

Nirajan Dhakal - nirajandhakal634@gmail.com

Project Link: [https://github.com/Neerazan/student_entry](https://github.com/Neerazan/student_entry)
