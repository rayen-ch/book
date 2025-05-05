# Django Shop Project

## Introduction

This project is a Django-based online shop. It includes functionalities for user management, product listings, product reviews, shopping cart, and an admin panel.

## Table of Contents

- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Running the Project](#running-the-project)
- [Contributing](#contributing)
- [Branching Workflow](#branching-workflow)

## Project Structure

    django-shop-project/
    ├── myshop/
    | ├── core/
    | ├── users/
    | ├── products/
    | ├── reviews/
    | ├── cart/
    | ├── admin_panel/ 
    | ├── init.py
    | ├── settings.py
    | ├── urls.py
    | ├── wsgi.py
    | ├── asgi.py
    ├── manage.py
    └── README.md


## Getting Started

### Prerequisites

- Python 3.x
- Git
- Virtualenv (optional but recommended)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/django-shop-project.git
   cd django-shop-project

   ```

2. Create and Activate Virtual Environment

- On MacOS/Linux:

      python3 -m venv venv
      source venv/bin/activate

- On Windows:

      python3 -m venv venv
      source venv/bin/activate

3.  Install requirements

        pip install -r requirements.txt

4.  Set Up Django

- Run migrations to set up the database schema:
  python manage.py migrate

5. Create a Superuser

- Create an admin account to access the Django admin panel

      python manage.py migrate

6. Collect Static Files

- Collect all static files into the `STATIC_ROOT´ directory:
  python manage.py collectstatic

### Running the Project

1. Run the Development Server

- Start the Django development server:

      python manage.py runserver

- Open your browser and go to `http://127.0.0.1:8000/´ to view the project.

### Contributing

To contribute to this project, follow these steps:

1. Fork the Repository

- Click the "Fork" button on the top right of the repository page on GitHub.

2. Clone Your Fork

- Clone your forked repository to your local machine:

      git clone https://github.com/yourusername/django-shop-project.git
      cd django-shop-project

3. Create a New Branch

- Create a new branch for your feature or bug fix:

      git checkout -b feature/your-feature-name

4. Make Changes

- Make your changes and commit them with a descriptive message:

      git add .
      git commit -m "Add your descriptive commit message"

5. Push to Your Fork

- Push your branch to your forked repository:

      git push origin feature/your-feature-name

6. Create a Pull Request

- Go to the original repository on GitHub and click on the "New Pull Request" button.
- Select your branch and create a pull request with a descriptive title and detailed description

### Branching Workflow

- main: The stable production branch.
- feature/your-feature-name: Feature branches for new features.
- bugfix/your-bugfix-name: Bug fix branches for fixing issues.
