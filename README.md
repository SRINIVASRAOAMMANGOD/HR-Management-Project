# HR Management System
```
A web-based HR Management System built using Django.This platform allows HR users to manage employee data,
update profiles, upload profile photos, andexport employee details in CSV or Excel formats.
```

## Features
```
- User Authentication (Sign Up, Login, Logout)
- HR Dashboard to manage employees
- Add/Edit/Delete Employee Records
- Upload Profile Image using Cloudinary
- Export Employee Data (CSV & Excel)
- Deployed on Render
```
## Tech Stack

- Python 3.13
- Django 5.2.3
- SQLite / PostgreSQL (via `dj_database_url`)
- HTML5, CSS3, Bootstrap 4+
- Cloudinary (for image storage)
- Render (for deployment)

## Project Structure
```
hr/
├── hr/  # Project settings
├── hrapp/ # Core app
├── static/ # CSS, JS, etc.
├── templates/ # HTML files
├── media/ # Uploaded media (for local dev)
├── requirements.txt
└── README.md
```

##  Installation (For Local Development)

```bash
Clone the repository
git clone https://github.com/yourusername/hr-management.git
cd hr-management

Create a virtual environment
python3 -m venv venv
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Migrate and run
python manage.py migrate
python manage.py runserver
```

## Deployment on Render
```
- Ensure these are set in your .env or Render Environment Variables
- CLOUD_NAME=your_cloud_name
- API_KEY=your_api_key
- API_SECRET=your_api_secret
- DEBUG=False
- SECRET_KEY=your_django_secret
```
