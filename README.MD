# Railway Management System

A comprehensive Railway Management System built with Django. Features include train scheduling, secure ticket booking, PNR status checks, and user authentication. Recently upgraded to Django 5 with SQLite support for easy deployment and a modernized UI. Created and maintained by Bishal Thakur.

## How to Run

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Initialize Database** (First time only):
    ```bash
    python manage.py migrate
    python init_db.py
    ```

3.  **Run Server**:
    ```bash
    python manage.py runserver
    ```

4.  **Access**: Open `http://127.0.0.1:8000/` in your browser.

## Credentials

- **Username**: `thabishal0`
- **Password**: `1234567890`
