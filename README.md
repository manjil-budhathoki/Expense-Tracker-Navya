# Expense Tracker Project

## 1. Project Setup Steps
These are the commands and configurations we used to set up the foundation.

1. **Created Environment:**
   `conda create --name tracker_env python=3.10`
   `conda activate tracker_env`

2. **Installed Django:**
   `pip install django`

3. **Created Project:**
   `django-admin startproject expense_tracker .`

4. **Created App:**
   `python manage.py startapp expenses`

5. **Configured Settings (`settings.py`):**
   - Added `'expenses'` to `INSTALLED_APPS`.
   - Added `AUTH_USER_MODEL = 'expenses.CustomUser'`.

6. **Created Custom User (`expenses/models.py`):**
   - Added `CustomUser` class inheriting from `AbstractUser`.