# MyProject — Django Templates + MySQL

## Stack
- Django 5 + Django Templates
- MySQL via pymysql
- Session-based authentication

---

## Setup

```bash
# 1. Create and activate virtual environment
python -m venv env

# Windows:
env\Scripts\activate
# Mac/Linux:
source env/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Open .env and fill in your MySQL credentials

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create superuser (admin account)
python manage.py createsuperuser

# 6. Collect static files
python manage.py collectstatic --noinput

# 7. Run the server
python manage.py runserver
```

## URLs
- http://127.0.0.1:8000/login/            → Login page
- http://127.0.0.1:8000/register/         → Register page
- http://127.0.0.1:8000/dashboard/        → User panel (login required)
- http://127.0.0.1:8000/management/       → Admin panel (admin role required)
- http://127.0.0.1:8000/admin/            → Django built-in admin

## Team Git Workflow
1. Clone the repo
2. Follow setup above
3. Create a feature branch: `git checkout -b feature/your-feature`
4. Open a Merge Request on GitLab into `main`
