# Structural Portfolio UK - Django Advanced

A professional portfolio showcasing structural engineering projects designed during my 8 years working in the UK.  
Developed for **SoftUni Django Advanced Regular Exam – April 2026**.

## Features

### Web Application
- Public project catalog with details, images, and design team
- Responsive design with Bootstrap 5
- Full CRUD operations for projects (Create, Read, Update, Delete)
- Advanced filtering by year, construction type, and designer
- Statistics page with key metrics
- Custom 404 error page

### Authentication & Authorization
- Custom User model extending `AbstractUser`
- OneToOne Profile model with avatar and bio
- User registration, login, and logout
- Group-based permissions (`Administrators` and `Viewers`)
- Custom mixin (`AdministratorRequiredMixin`) for protected views

### REST API
- Public project list and detail endpoints
- Authenticated profile endpoint
- Designer list endpoint

### Advanced Features
- Asynchronous welcome email using **Celery** + Redis after registration
- Media file handling (project images and profile avatars)
- Comprehensive test coverage (13 passed + 2 skipped)

## Technologies

- **Backend**: Django 5.2.10
- **Database**: PostgreSQL
- **Authentication**: Custom User Model + Groups
- **API**: Django REST Framework
- **Async Tasks**: Celery + Redis
- **Frontend**: Bootstrap 5 (via CDN)
- **Testing**: Django Test + REST Framework APITestCase
- **Environment Management**: python-dotenv

## Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/IfSD77/struct-portfolio-uk-advanced.git
   cd struct-portfolio-uk-advanced
2. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Configure environment variables:
   - Copy .env.template to .env
   - Fill in your PostgreSQL credentials (DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT) and SECRET_KEY
5. Create a database and apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
6. Start Redis (in a separate terminal):
   ```bash
   redis-server --port 6380
7. Start Celery worker (in another terminal):
   ```bash
   celery -A struct_portfolio_advanced worker --pool=solo --loglevel=info
8. Start a Django development server:
   ```bash
   python manage.py runserver
   Open: http://127.0.0.1:8000/
9. Running Tests
   ```bash
   python manage.py test accounts -v 2

## Project Structure:
   - accounts/ – CustomUser, Profile, authentication views, forms and API
   - projects/ – Main models, views, forms, templates and API
   - designers/ & participations/ – Many-to-Many relationship implementation
   - templates/ – All HTML templates with base inheritance
   - static/ – Custom CSS (if any)

## Notes
   - Public pages do not require authentication (extended from Basics project)
   - Only users in the Administrators group can create, edit or delete projects
   - Viewers group can only browse the catalog
   - Uploaded images are stored in the media/ folder (not committed to Git)