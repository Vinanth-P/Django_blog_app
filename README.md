# Django Blog App

![Django Blog Preview](demo.gif)

> A full-featured, production-ready blogging web application built with Python 3.12 and Django 5.0. Features custom user authentication, profile management with avatars, paginated post feeds, author-restricted CRUD operations, and Bootstrap styling.

## ✨ Features

- 🔐 **User Authentication**: Secure registration, login, logout, and password reset functionality.
- 👤 **Custom User Profiles**: User profiles with custom avatar image uploading and email/username management.
- 📰 **Paginated Feed**: Clean article list with pagination (`First`, `Previous`, `Next`, `Last`).
- ✍️ **Full CRUD Operations**: Create, read, update, and delete posts (restricted to post authors).
- 🎨 **Responsive UI**: Steel-blue navbar layout with sidebars and flash message alerts.

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/Vinanth-P/Django_blog_app.git
cd Django_blog_app
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install django pillow
```

### 4. Run migrations & load sample data
```bash
python manage.py migrate
```

### 5. Start the server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.
