# Apartment Management System - Backend

Simple Django + Django REST Framework backend with 3 modules:
- **Visitors** – `/api/visitors/`
- **Parking** – `/api/parking/`
- **Fire & Safety** – `/api/firesafety/`

## Run locally

```bash
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser   # optional, for /admin/

python manage.py runserver
```

Visit `http://127.0.0.1:8000/api/visitors/` (or parking / firesafety) to test.

## Push to your own GitHub repo

1. Create an **empty** repo on GitHub (don't add a README/gitignore there — this project already has them).
2. In this folder, run:

```bash
git init
git remote add origin https://github.com/<your-username>/<your-repo>.git
git add .
git commit -m "Initial Django backend for apartment management"
git branch -M main
git push -u origin main
```

3. When prompted for a password, paste your GitHub **Personal Access Token** (not your account password).

## Deploy later (EC2 + Gunicorn + Nginx)

```bash
pip install gunicorn
gunicorn apartment_backend.wsgi:application --bind 0.0.0.0:8000
```

Then point Nginx to proxy requests to `127.0.0.1:8000`.
