# Structural Portfolio UK - Django Advanced

A professional portfolio showcasing structural engineering projects designed during my 8 years working in the UK.  
Developed for **SoftUni Django Advanced Regular Exam – April 2026**.

## Features

### Web Application
- Public project catalog with details, images and design team
- Responsive design with Bootstrap 5
- Full CRUD operations for projects (Create, Read, Update, Delete)
- Statistics page with key metrics
- Custom 404 and 500 error pages
- Projects filtered by construction type

### Authentication & Authorization
- Custom User model extending `AbstractUser`
- OneToOne Profile model
- User registration, login and logout
- Group-based permissions (`Administrators` and `Viewers`)
- Protected views for administrators only

### Advanced Features
- Asynchronous welcome email sent via **Celery + Redis** (with graceful degradation)
- Proper media file handling for project images
- Comprehensive test suite

## Technologies
- **Backend**: Django 5.2
- **Database**: SQLite (production)
- **Python Version**: 3.12.3 (production)
- **Frontend**: Bootstrap 5
- **Web Server**: Nginx + Gunicorn
- **Async Tasks**: Celery + Redis

## Local Setup

1. Clone the repository

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Apply migrations and create superuser:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser

5. Run the development server:
   ```bash
   python manage.py runserver

## Project Structure
- `accounts/` – CustomUser, Profile, authentication and forms
- `projects/` – Main models, views, forms and templates
- `designers/` & `participations/` – Many-to-Many relationship
- `templates/` – All HTML templates with base inheritance

## Deployment

The project is deployed on **AWS EC2** (Ubuntu 24.04).

- **Web Server**: Nginx (reverse proxy)
- **Application Server**: Gunicorn (3 workers)
- **Database**: SQLite
- **Static Files**: Served by Nginx + WhiteNoise
- **Live URL**: http://13.63.72.6

## Deployment Details
- Gunicorn is managed as a systemd service
- Nginx acts as reverse proxy
- The application starts automatically on server boot

**Note**: Django admin interface is functional. The main public functionality works as expected.

## How to Access
- **Public website**: http://13.63.72.6
- **Admin panel**: http://13.63.72.6/admin/

**Important**:
- Only users in the **Administrators** group can create, edit or delete projects.
- Viewers group can only browse the catalog.

## Notes
- Public pages are accessible to anonymous users
- Uploaded images are stored in the `media/` folder
- Celery tasks are handled gracefully if Redis is unavailable
