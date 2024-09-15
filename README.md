# Student Entry System

A Django-based web application for managing student records with integration of Django Rest Framework (DRF) for API access. This project allows administrators to create, update, and delete student records through a web interface and exposes the student model through a REST API.

## Features

- **Student Model:** Manages student information including Name, Age, Address, Grade, and Major.
- **Admin Interface:** Record new student details, update existing records, and delete records.
- **REST API:** Exposes student model via a REST API for CRUD operations.
- **Port Configuration:** Runs on `localhost` at port `8025`.

## Project Setup

### Prerequisites

- Python 3.8 or later
- Pipenv for virtual environment management

### Installation

1. **Clone the Repository:**
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set up Virtual Environment:**
   ```sh
   pipenv install
   pipenv shell
   ```

3. **Install Dependencies:**
   ```sh
   pipenv install django djangorestframework
   ```

4. **Apply Migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Create Superuser (for admin access):**
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the Development Server:**
   ```sh
   python manage.py runserver 8025
   ```

## Usage

### Admin Interface

1. Access the admin interface at `http://localhost:8025/admin/`
2. Log in using the superuser credentials created earlier
3. Navigate to the Students section to manage student records

### REST API

The REST API endpoints are available at:

- List/Create: `http://localhost:8025/api/students/`
- Retrieve/Update/Delete: `http://localhost:8025/api/students/<id>/`

Use appropriate HTTP methods (GET, POST, PUT, DELETE) to interact with the API.

## API Documentation

For detailed API documentation, visit `http://localhost:8025/api/docs/` after starting the development server.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` file for more information.

## Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/student-entry-system](https://github.com/yourusername/student-entry-system)