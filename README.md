# 🚀 Alx Django Learning Lab

> *A comprehensive learning resource for mastering Django - From fundamentals to production-ready applications*

[![ALX](https://img.shields.io/badge/ALX-Software_Engineering-00d4ff?style=flat-square)](https://www.alxafrica.com/)
[![Django](https://img.shields.io/badge/Django-Latest-092e20?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776ab?style=flat-square&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## 📖 About

Welcome to **Alx Django Learning Lab**! This repository is a comprehensive learning resource for mastering **Django**, a powerful and popular Python web framework.

This repository contains projects, exercises, and examples designed to help you learn Django from the ground up. Whether you're a beginner or looking to deepen your Django skills, you'll find practical examples and hands-on projects here.

---

## 🎯 Learning Objectives

Through this lab, you will:

- ✅ **Understand Django's MVT Architecture** - Master Model-View-Template design pattern
- ✅ **Django ORM Mastery** - Object-Relational Mapping for seamless database interactions
- ✅ **Build Robust REST APIs** - Create powerful APIs with Django REST Framework
- ✅ **User Authentication & Authorization** - Implement secure login systems and permissions
- ✅ **Forms, Validators & Middleware** - Handle user input and request/response processing
- ✅ **Deploy Django Applications** - Take your apps from development to production
- ✅ **Best Practices & Design Patterns** - Write clean, maintainable Django code

---

## 📂 Repository Structure

```
Alx_DjangoLearnLab/
├── 📁 0x1.Introduction_to_Django/
│   └── LibraryProject/          # First Django project
│
├── 📁 django-models/
│   └── relationship_app/        # Model relationships & ORM
│
├── 📁 django_blog/              # Blog application project
│
├── 📁 advanced_features_and_security/
│   └── LibraryProject/          # Security & advanced features
│
├── 📁 social_media_api/         # REST API project
│
├── 📁 api_project/              # API development basics
│
├── 📁 advanced_api_project/     # Advanced API concepts
│
└── 📄 README.md                 # You are here
```

---

## 🛠️ Setup & Installation

### Prerequisites

- **Python 3.x** or higher
- **pip** (Python package manager)
- **virtualenv** (recommended)
- **Git**
- **SQLite** (default) or **PostgreSQL** (for production)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/medob6/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab

# Create and activate virtual environment
python3 -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Install Django (if requirements.txt exists)
pip install -r requirements.txt
# Or install Django directly
pip install django djangorestframework

# Navigate to a project
cd 0x1.Introduction_to_Django/LibraryProject

# Run migrations
python manage.py migrate

# Create superuser (optional but recommended)
python manage.py createsuperuser

# Start development server
python manage.py runserver

# Visit http://127.0.0.1:8000 in your browser
```

---

## 📚 Projects Overview

### 1. 📖 LibraryProject
**Location**: `0x1.Introduction_to_Django/LibraryProject/`

Your first Django project! Learn the fundamentals:
- Django project structure
- Basic MVT pattern
- URL routing and views
- Template rendering

**Run it:**
```bash
cd 0x1.Introduction_to_Django/LibraryProject
python manage.py runserver
```

---

### 2. 🔗 Relationship App
**Location**: `django-models/relationship_app/`

Master Django models and database relationships:
- One-to-Many relationships
- Many-to-Many relationships
- Foreign Keys
- Django ORM queries
- Model methods and properties

**Key Concepts:**
```python
# Example model relationships
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

---

### 3. 📝 Django Blog
**Location**: `django_blog/`

A full-featured blogging platform:
- User authentication (register, login, logout)
- CRUD operations for blog posts
- Comments system
- User profiles
- Categories and tags
- Search functionality

**Features:**
- ✍️ Create and edit posts
- 💬 Comment on posts
- 👤 User profiles
- 🔍 Search posts
- 📱 Responsive design

---

### 4. 🔐 Advanced Features & Security
**Location**: `advanced_features_and_security/LibraryProject/`

Learn Django security best practices:
- CSRF protection
- SQL injection prevention
- XSS protection
- Authentication backends
- Permission systems
- Custom user models
- Security middleware

**Security Topics:**
- User permissions and groups
- Content Security Policy
- Secure password handling
- HTTPS configuration

---

### 5. 🌐 Social Media API
**Location**: `social_media_api/`

Build a social networking REST API:
- User registration and authentication
- Posts and comments
- Follow/Unfollow system
- Like/Unlike functionality
- News feed algorithm
- API documentation with Swagger

**API Endpoints:**
```
POST   /api/auth/register/
POST   /api/auth/login/
GET    /api/posts/
POST   /api/posts/
GET    /api/users/{id}/followers/
POST   /api/posts/{id}/like/
```

---

### 6. 🔌 API Project
**Location**: `api_project/`

Introduction to Django REST Framework:
- Serializers
- ViewSets and Routers
- API views
- Authentication and permissions
- Filtering and pagination

**Learn:**
- Creating RESTful endpoints
- JSON serialization
- Token authentication
- API versioning

---

### 7. 🚀 Advanced API Project
**Location**: `advanced_api_project/`

Advanced API development techniques:
- Custom permissions
- Nested serializers
- API throttling
- Caching strategies
- API documentation
- Testing APIs

---

## 🔧 Essential Django Commands

```bash
# Project Management
django-admin startproject myproject    # Create new project
python manage.py startapp myapp        # Create new app
python manage.py runserver            # Start dev server
python manage.py runserver 0.0.0.0:8000  # Run on all interfaces

# Database
python manage.py makemigrations       # Create migrations
python manage.py migrate              # Apply migrations
python manage.py showmigrations       # Show migration status
python manage.py sqlmigrate app 0001  # Show SQL for migration

# User Management
python manage.py createsuperuser      # Create admin user
python manage.py changepassword user  # Change user password

# Development
python manage.py shell                # Django Python shell
python manage.py dbshell              # Database shell
python manage.py check                # Check for issues
python manage.py test                 # Run tests

# Static Files
python manage.py collectstatic        # Collect static files
python manage.py findstatic file.css  # Find static file location

# Utilities
python manage.py dumpdata > data.json # Export data
python manage.py loaddata data.json   # Import data
python manage.py flush                # Clear database
```

---

## 📖 Key Concepts Explained

### 🏗️ MVT Architecture

```python
# MODEL (models.py) - Data layer
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# VIEW (views.py) - Logic layer
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# TEMPLATE (post_list.html) - Presentation layer
# {% for post in posts %}
#   <h2>{{ post.title }}</h2>
#   <p>{{ post.content }}</p>
# {% endfor %}
```

### 🔗 URL Routing

```python
# urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post-list'),
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('api/', include('api.urls')),
]
```

### 📊 Django ORM

```python
# Create
post = Post.objects.create(title="My Post", content="Content here")

# Read
all_posts = Post.objects.all()
post = Post.objects.get(id=1)
filtered = Post.objects.filter(author__username='john')

# Update
post.title = "Updated Title"
post.save()

# Delete
post.delete()

# Complex queries
posts = Post.objects.filter(
    created_at__year=2024
).select_related('author').prefetch_related('comments')
```

---

## 🧪 Testing Your Applications

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test myapp

# Run with verbosity
python manage.py test --verbosity=2

# Keep database after tests
python manage.py test --keepdb

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

**Writing Tests:**
```python
from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title="Test Post", content="Test")
    
    def test_post_creation(self):
        post = Post.objects.get(title="Test Post")
        self.assertEqual(post.content, "Test")
```

---

## 📚 Learning Resources

### 📖 Official Documentation
- [Django Documentation](https://docs.djangoproject.com/) - Comprehensive official docs
- [Django REST Framework](https://www.django-rest-framework.org/) - API development
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/) - Official tutorial

### 🎥 Video Tutorials
- [Django For Everybody - Dr. Chuck](https://www.dj4e.com/)
- [Django Crash Course - Traversy Media](https://www.youtube.com/watch?v=e1IyzVyrLSU)
- [Python Django Web Framework - freeCodeCamp](https://www.youtube.com/watch?v=F5mRW0jo-U4)

### 📝 Blogs & Articles
- [Real Python - Django Tutorials](https://realpython.com/tutorials/django/)
- [Django Best Practices](https://django-best-practices.readthedocs.io/)
- [Simple is Better Than Complex](https://simpleisbetterthancomplex.com/)

### 💬 Community
- [Django Forum](https://forum.djangoproject.com/)
- [Stack Overflow - Django](https://stackoverflow.com/questions/tagged/django)
- [Reddit - r/django](https://www.reddit.com/r/django/)
- [Django Discord](https://discord.gg/xcRH6mN4fa)

---

## 💡 Best Practices

### 🔐 Security
```python
# settings.py - Use environment variables
import os
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')

# Never commit sensitive data
# Use .env files (add to .gitignore)
```

### 🗃️ Database Optimization
```python
# Use select_related for ForeignKey
posts = Post.objects.select_related('author').all()

# Use prefetch_related for ManyToMany
posts = Post.objects.prefetch_related('tags').all()

# Index frequently queried fields
class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
```

### 📦 Project Structure
```python
# Keep apps focused and reusable
# Good app names: blog, users, api, core
# Each app should have a single responsibility
```

### 🧹 Code Quality
```python
# Use Django's built-in tools
# Follow PEP 8 style guide
# Write docstrings
# Use type hints (Python 3.5+)

def get_user_posts(user_id: int) -> QuerySet:
    """
    Retrieve all posts for a given user.
    
    Args:
        user_id: The ID of the user
    
    Returns:
        QuerySet of Post objects
    """
    return Post.objects.filter(author_id=user_id)
```

---

## 🚀 Deployment Guide

### Preparation Checklist

- [ ] Set `DEBUG = False` in production
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use environment variables for secrets
- [ ] Set up PostgreSQL or MySQL (not SQLite)
- [ ] Configure static and media files
- [ ] Set up email backend
- [ ] Enable HTTPS
- [ ] Configure CSRF settings
- [ ] Set up logging
- [ ] Run security checks

### Security Check
```bash
python manage.py check --deploy
```

### Popular Deployment Options
- **Heroku** - Easy deployment for beginners
- **DigitalOcean** - VPS with more control
- **AWS Elastic Beanstalk** - Scalable deployment
- **Railway** - Modern deployment platform
- **Render** - Simple and powerful

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines
- Follow Django coding style
- Write meaningful commit messages
- Add tests for new features
- Update documentation
- Keep pull requests focused

---

## 📜 License

This project is part of the ALX Software Engineering program. Feel free to use it for learning purposes.

---

## 👤 Author

**medob6**

- 🐙 GitHub: [@medob6](https://github.com/medob6)
- 📧 Email: [your-email@example.com]
- 💼 LinkedIn: [Your LinkedIn Profile]
- 🌐 Portfolio: [your-website.com]

---

## 🙏 Acknowledgments

- **ALX Africa** for providing this incredible learning opportunity
- **Django Software Foundation** for maintaining this excellent framework
- **The Django Community** for extensive documentation and support
- **Fellow ALX Learners** for collaboration and mutual growth

---

## 📈 Learning Progress Tracker

Track your progress through the repository:

### Fundamentals
- [ ] Complete Introduction to Django
- [ ] Understand MVT architecture
- [ ] Master URL routing and views
- [ ] Learn template system

### Models & Database
- [ ] Create models and migrations
- [ ] Understand model relationships
- [ ] Master Django ORM queries
- [ ] Customize admin interface

### Forms & Validation
- [ ] Work with Django forms
- [ ] Implement form validation
- [ ] Handle file uploads
- [ ] Use ModelForms

### Authentication
- [ ] User registration and login
- [ ] Password reset functionality
- [ ] Custom user models
- [ ] Permissions and groups

### REST APIs
- [ ] Build basic REST API
- [ ] Use Django REST Framework
- [ ] Implement authentication
- [ ] Add API documentation

### Advanced Topics
- [ ] Implement security measures
- [ ] Optimize database queries
- [ ] Add caching
- [ ] Deploy application

---

<div align="center">

## 🌟 **Happy Learning & Keep Building!**

*"The best way to learn Django is by building real projects"*

⭐ **Star this repo** if you find it helpful!

📖 **Follow along** with your Django journey

🤝 **Share** with fellow learners

---

**[⬆ back to top](#-alx-django-learning-lab)**

</div>
