# Structural Portfolio - UK
A personal catalog of structural engineering projects designed during my 8 years working in UK.  
This project was developed for the **SoftUni Django Basics Regular Exam** – February 2026.

## Features
- Project catalog with details (name, year completed, location, contract value, description, main image)
- Design team (designers/engineers/architects) with roles via ManyToMany relationship
- Public forms for adding, editing, and deleting projects (no authentication required)
- Delete confirmation step
- Filtering projects by year and construction type
- Basic statistics (total projects, total value, average value)
- Custom 404 page
- Responsive Bootstrap 5 design
- PostgreSQL database

## Local Setup
1. Clone the repository: 
    - [git clone](https://github.com/IfSD77/Django-Basics---Individual-Project.git)
    - cd struct-portfolio-uk
2. Create and activate virtual environment:
    - python -m venv .venv
    - .venv\Scripts\activate
3. Install dependencies:
    - pip install -r requirements.txt
4. Configure PostgreSQL:
    - Create database `struct_portfolio`
    - Update `DATABASES` in `struct_portfolio_uk/settings.py` (user, password, host, port)
5. Apply migrations and create superuser:
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py createsuperuser
6. Start server:
    - python manage.py runserver
    - Open in browser: http://127.0.0.1:8000/
    - Admin: /admin/
    - Add projects: /projects/add/
    - Uploaded images saved to `media/` (not in git)

## Technologies
    - Django 5.2
    - PostgreSQL
    - Bootstrap 5 (CDN)
    - Pillow (ImageField)

## Notes
    - No authentication (exam requirement)
    - Images are local only (upload via form/admin)
    - Original project based on real UK experience