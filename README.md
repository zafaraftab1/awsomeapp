SocialMediaClone
=================

A small Django-based social media clone project (development workspace).

Contents
--------
- Project overview
- Quick setup and run instructions
- Common commands
- Notes about media/static files and templates

Project overview
----------------
This repository contains a Django project named `SocialMediaProject` and an app `SocialMedia`. It includes templates, static assets, and a sqlite3 database used for local development. Use this README to get the project running locally for development and testing.

Prerequisites
-------------
- Python 3.10+ (or a supported 3.x version listed in `requirements.txt`)
- pip
- virtualenv or venv
- (Optional) PostgreSQL/MySQL if you want to switch from the provided sqlite3

Quick setup (macOS / zsh)
-------------------------
1. Open a terminal and change into the repository root:

```bash
cd /Users/zafaraftab/PycharmProjects/SocialMediaClone
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. (Optional) Create a superuser to access the admin:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Open http://127.0.0.1:8000/ in your browser.

Notes about the bundled sqlite database
--------------------------------------
A `db.sqlite3` file may already be present for convenience in development. If you want a fresh database, remove `db.sqlite3` and rerun migrations.

Media and static files
----------------------
- Media files are stored under the `media/` directory in the repository root (used for development only).
- Static files and templates are present in `static/` and `templates/` respectively. In production, configure proper static/media hosting (e.g., S3, CDN).

Testing
-------
Run Django tests with:

```bash
python manage.py test
```

Troubleshooting
---------------
- If you get dependency or import errors, confirm the virtualenv is activated and `pip install -r requirements.txt` completed successfully.
- If migrations fail, inspect the output and consider running `python manage.py makemigrations` and then `migrate`.

Useful commands
---------------
- Run shell: `python manage.py shell`
- Collect static (for production staging): `python manage.py collectstatic --noinput`

Contributing
------------
Small contributions and documentation improvements are welcome. Please follow common GitHub/Git practices (feature branch, tests, PR description).

License & contact
-----------------
This project should include a license file if you plan to distribute it. Add `LICENSE` at the repo root and update this section with your preferred license and contact information.


--
Generated README for local development. Update any paths or commands to match your environment and deployment setup.
