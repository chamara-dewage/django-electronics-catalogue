# Electronics Product Catalogue

A Django-based electronics product catalogue that allows users to browse products, search by keywords, filter by category and tags, sort results, and navigate through paginated product listings.

## Features

- **Product catalogue:** Displays products with their name, description, price, category, and tags.
- **Product search:** Search products using keywords in product names, descriptions, and category names.
- **Category filtering:** Filter products by category.
- **Tag filtering:** Filter products by tag.
- **Combined filtering:** Apply search, category, tag, and sorting options together.
- **Sorting:** Sort products by name or price in ascending or descending order.
- **Pagination:** Display five products per page, with navigation between pages.
- **Django Admin:** Manage products, categories, and tags through the Django administration interface.

## Technologies Used

- Python
- Django 5.2.19
- SQLite
- HTML

## Project Structure

```text
django-takehome/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── products/
│   ├── management/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── templates/
│   └── products.html
│
├── requirements.txt
├── manage.py
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_PUBLIC_REPOSITORY_URL
cd django-takehome
```

Replace `YOUR_PUBLIC_REPOSITORY_URL` with the URL of the public GitHub or GitLab repository.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create a Django administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your username and password.

### 7. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

## Django Admin

Access the administration interface at:

http://127.0.0.1:8000/admin/

Log in using the superuser account created during setup.

Use the admin interface to manage:

- Categories
- Tags
- Products

The project sample data includes:

- 5 categories
- 10 tags
- 20 products

If starting with a fresh database, add the sample records through the Django Admin interface.

## Using the Product Catalogue

1. Open the home page.
2. Enter a keyword in the search field to find products.
3. Select a category to filter products.
4. Select a tag to filter products.
5. Choose a sorting option to order the results by product name or price.
6. Click the apply button to display the results.
7. Use the pagination links to navigate between product pages.

Search, category filtering, tag filtering, and sorting can be combined.

## Database

The application uses SQLite as its database.

Django migrations are used to create and manage the database schema.

## Notes

- The application is intended for local development and demonstration.
- The default pagination size is five products per page.
- Product, category, and tag records can be managed through Django Admin.
