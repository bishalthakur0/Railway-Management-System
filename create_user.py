import os
import django
import sqlite3

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lorax.settings")
django.setup()

from django.contrib.auth.models import User

USERNAME = "thabishal0"
EMAIL = "thabishal0@gmail.com"
PASSWORD = "1234567890"
ADDRESS = "Unknown"

def create_user():
    # 1. Create Django User
    if User.objects.filter(username=USERNAME).exists():
        print(f"User {USERNAME} already exists. Updating password.")
        user = User.objects.get(username=USERNAME)
        user.set_password(PASSWORD)
        user.email = EMAIL
        user.save()
    else:
        print(f"Creating user {USERNAME}...")
        User.objects.create_user(username=USERNAME, email=EMAIL, password=PASSWORD)

    # 2. Create Account in Custom Table (for FK constraints)
    # The Account table has Username varchar(15). 'thabishal0' is 10 chars.
    
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    
    # Check if exists in Account
    c.execute("SELECT * FROM Account WHERE Username=?", (USERNAME,))
    if c.fetchone():
        print(f"Account for {USERNAME} already exists in SQL table.")
        # Update if needed?
    else:
        print(f"Inserting {USERNAME} into Account table...")
        # Schema: Username, Password, Email_Id, Address
        c.execute("INSERT INTO Account (Username, Password, Email_Id, Address) VALUES (?, ?, ?, ?)", 
                  (USERNAME, PASSWORD, EMAIL, ADDRESS))
        conn.commit()
    
    conn.close()
    print("User creation/update complete.")

if __name__ == "__main__":
    create_user()
