# Store-Market

Store-Market is a scalable and secure eCommerce application built using Django and Django REST Framework (DRF). The backend handles user authentication, product management, and order processing efficiently, with data stored in an SQL database (e.g., MySQL). The application is designed to support high performance and scalability, using robust deployment techniques and stress-testing tools.

## Features

- **User Authentication**: Secure user authentication and authorization using JSON Web Tokens (JWT).
- **Product Management**: APIs for creating, updating, and managing product catalogs.
- **Order Processing**: Endpoints for placing and managing orders.
- **Stress and Performance Testing**: Load testing with Locust.
- **Automation Testing**: Automated API tests using Pytest.
- **Dependency Management**: Managed using Pipenv.

## Backend Technology Stack

- **Django**: A powerful Python web framework for rapid development.
- **Django REST Framework (DRF)**: Simplifies the creation of RESTful APIs.
- **SQL Database**: MySQL as the database backend for efficient data handling.
- **Authentication**: JWT for secure user sessions.
- **Deployment**: 
  - Windows Server deployment using Gunicorn and Windows Services.

## Installation

### Prerequisites

- Python 3.8+
- MySQL
- Pipenv

### Setup

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/J0-Y0/GO2COD-FS-02.git
    cd store-market
    ```

2. **Set Up Virtual Environment**:

    Install Pipenv if not already installed:

    ```bash
    pip install pipenv
    ```

    Create and activate a virtual environment:

    ```bash
    pipenv install
    pipenv shell
    ```

3. **Install Dependencies**:

    ```bash
    pipenv install
    ```

4. **Set Up the Database**:

    Configure the `DATABASES` setting in `core/settings/dev.py` for development and `core/settings/prod.py` for production to match your MySQL database:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'store_market',
            'USER': 'your_username',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

    Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. **Run the Server**:

    ```bash
    python manage.py runserver
    ```

6. **Create a Superuser**:

    ```bash
    python manage.py createsuperuser
    ```

7. **Run Tests**:

    Run automated tests using Pytest:

    ```bash
    pytest
    ```

8. **Stress Testing**:

    Install Locust for load testing:

    ```bash
    pipenv install locust
    ```

    Run Locust:

    ```bash
    locust
    ```

## Deployment on Windows Server

### Prerequisites

- Gunicorn
- Windows Server
- Task Scheduler (or a service manager like NSSM)

### Steps

1. **Install Gunicorn**:

    ```bash
    pipenv install gunicorn
    ```

2. **Run Gunicorn Manually**:

    ```bash
    gunicorn core.wsgi:application --bind 0.0.0.0:8000
    ```

3. **Set Up Gunicorn as a Windows Service**:

    Use a service manager like NSSM (Non-Sucking Service Manager) to run Gunicorn as a service.

    - Download and install NSSM.
    - Create a new service:

      ```cmd
      nssm install StoreMarketGunicorn
      ```

    - Set the `Path` to the Gunicorn executable:

      ```cmd
      C:\Users\<your_username>\.virtualenvs\store-market\Scripts\gunicorn.exe
      ```

    - Set the `Startup directory` to the project root.
    - Set the `Arguments` to:

      ```
      core.wsgi:application --bind 0.0.0.0:8000
      ```

    - Start the service:

      ```cmd
      nssm start StoreMarketGunicorn
      ```

4. **Serve Static Files**:

    Configure the Django settings to use `django.contrib.staticfiles` for serving static content during development. For production, use a separate web server (like IIS) to serve static files.

5. **Set Up IIS for Static Files (Optional)**:

    - Configure IIS to handle requests for `/static/` and `/media/` by pointing to the respective directories in your project.

6. **Automate Server Start-Up**:

    Use Windows Task Scheduler to ensure Gunicorn starts automatically after a server reboot.

## Development Practices

- **Testing**: Pytest is used for unit and integration testing.
- **Performance**: Locust is utilized for stress testing to ensure the application performs well under load.
- **Dependency Management**: All dependencies are managed with Pipenv, ensuring consistent environments across development and production.

## Contributing

Contributions are welcome! Fork the repository and create a pull request with your changes. Ensure all tests pass before submitting.



## License

This project is open-source and available under the [MIT License](LICENSE).
