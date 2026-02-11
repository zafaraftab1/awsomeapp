SocialMediaClone
=================

A Django-based social media clone project intended as a development sandbox and starting point for learning and small prototypes.

High-level checklist
--------------------
- [x] Local development instructions (venv, install, migrate, run)
- [x] Environment variables and `.env.example`
- [x] Database options: sqlite3 (dev) and Postgres (prod/dev alternative)
- [x] Docker Compose example and quick production checklist
- [x] Testing, linting, and CI suggestions

Project overview
----------------
This repository contains a Django project named `SocialMediaProject` and a main app `SocialMedia`. It includes:

- Django project: `SocialMediaProject/`
- App: `SocialMedia/`
- Templates: `templates/`
- Static assets: `static/`
- Development media directory: `media/`
- A bundled `db.sqlite3` for quick local testing (optional)

Tech stack (from `requirements.txt`)
-----------------------------------
- Python 3.10+
- Django 5.2.x
- Django REST Framework
- django-allauth (authentication)
- djangorestframework-simplejwt (JWT tokens)
- Pillow (image handling)
- psycopg2 (Postgres client)

Prerequisites
-------------
- macOS / Linux / Windows
- Python 3.10 or newer
- pip
- virtualenv / venv
- (Optional) Docker & Docker Compose for containerized development

Environment variables
---------------------
Create a file named `.env` in the project root (do not check it into source control). See `.env.example` for the common variables used by this project. Key variables include:

- DJANGO_SECRET_KEY - Django SECRET_KEY for this project
- DJANGO_DEBUG - 'True' or 'False'
- DATABASE_URL - (optional) PostgreSQL URL, e.g. `postgres://user:pass@db:5432/dbname`
- ALLOWED_HOSTS - comma-separated hostnames for production

Local development (recommended)
-------------------------------
1. Open a terminal and change into the repository root:

```bash
cd /Users/zafaraftab/PycharmProjects/SocialMediaClone
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Upgrade pip and install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and edit values as needed (see `.env.example` for details).

```bash
cp .env.example .env
# edit .env with your editor
```

5. Apply database migrations (sqlite by default unless `DATABASE_URL` points to Postgres):

```bash
python manage.py migrate
```

6. (Optional) Load initial data or create a superuser:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

8. Open http://127.0.0.1:8000/ in your browser.

Using PostgreSQL locally
------------------------
If you prefer Postgres during development, set `DATABASE_URL` in `.env` to something like:

```
postgres://postgres:postgres@localhost:5432/socialdb
```

Install Postgres locally (e.g., via Homebrew on macOS):

```bash
brew install postgresql
brew services start postgresql
createdb socialdb
```

Then run migrations as normal:

```bash
python manage.py migrate
```

Docker Compose (example, not included as files)
-----------------------------------------------
Below is a minimal `docker-compose.yml` and `Dockerfile` outline you can use as a starting point. Add these files to the repo if you want containerized development.

docker-compose.yml (example):

```yaml
version: '3.8'
services:
  web:
    build: .
    command: gunicorn SocialMediaProject.wsgi:application --bind 0.0.0.0:8000
    env_file: .env
    ports:
      - '8000:8000'
    depends_on:
      - db
    volumes:
      - .:/code
      - media:/code/media
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: socialdb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
  media:
```

Dockerfile (example):

```dockerfile
FROM python:3.11-slim
WORKDIR /code
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "SocialMediaProject.wsgi:application", "--bind", "0.0.0.0:8000"]
```

Production checklist
--------------------
- Replace the default `SECRET_KEY` and keep it out of source control (use environment variables or a secrets manager).
- Set `DJANGO_DEBUG=False` and configure `ALLOWED_HOSTS`.
- Use a production-ready database (Postgres, MySQL).
- Configure static/media hosting (S3 or CDN) and run `collectstatic`.
- Use HTTPS (proxy/load balancer or web server).
- Configure application server (Gunicorn/uWSGI) + reverse proxy (Nginx).
- Add monitoring and logging (Sentry, Prometheus, etc.).
- Run migrations during deploy and keep backups of DB.

Security notes
--------------
- Never check `.env` or credentials into the repo.
- Use strong, unique `SECRET_KEY` and rotate if it leaks.
- Validate uploaded files and limit size (Pillow is installed for image handling).

Testing and quality
-------------------
Run Django tests:

```bash
python manage.py test
```

Linting / formatting suggestions:

```bash
pip install flake8 black isort
black .
flake8
```

Continuous Integration (CI)
---------------------------
A typical CI pipeline should include:
- Install dependencies
- Run linters and formatters
- Run tests
- Optionally run a minimal static type check (mypy) if you add types

Example GitHub Actions job snippet:

```yaml
# .github/workflows/ci.yml (example)
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install deps
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: python manage.py test --verbosity=2
```

Developer notes and troubleshooting
----------------------------------
- If migrations fail: run `python manage.py makemigrations` and inspect the migration files. Keep migrations in source control.
- If a dependency import error appears, ensure the virtualenv is active and `pip install -r requirements.txt` succeeded.
- If media files are missing locally, check the `media/` directory — it's included in this repo for convenience.

Contributing
------------
- Use feature branches and open pull requests.
- Add tests for new behavior and keep changes small.
- Document setup changes in this README.

License
-------
Add a `LICENSE` file at the project root and update this section with the chosen license.

Appendix: quick reference commands
---------------------------------
- Create virtualenv and activate:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

- Install dependencies:

```bash
pip install -r requirements.txt
```

- Apply migrations:

```bash
python manage.py migrate
```

- Run server:

```bash
python manage.py runserver
```

--
This README has been upgraded with advanced developer and deployment guidance. Update any placeholders (Docker, DATABASE_URL) to match your environment.
