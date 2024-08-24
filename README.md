# Hexashop

Hexashop is an e-commerce study-based web application built with Django. It offers a comprehensive shopping experience with features for user management, product listings, and cart functionalities.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)


## Features

- User authentication and registration
- Product catalog with categories
- Shopping cart functionality
- Order management
- Responsive design

## Installation

To get started with Hexashop, clone the repository and set up your environment:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/muhammadjalilov/Hexashop.git
    cd hexashop
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (optional):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Visit** `http://127.0.0.1:8000` in your web browser to view the application.

## Usage

- **Admin Interface:** Access the Django admin interface at `http://127.0.0.1:8000/admin` to manage products, categories, and users.
- **Cart Management:** Users can add products to their cart, view cart contents, and proceed to checkout.
- **Order Management:** Users can view their order history and details.

## Contributing

If you would like to contribute to the Hexashop project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

Please ensure that your code follows the existing coding style and includes appropriate tests.

