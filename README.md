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

7. **Use SQLite & Enable Auth System:**
   - These are enabled by default in Django settings.
   - Verified in `DATABASES` and `INSTALLED_APPS`.

## 2. Model & Database Steps

8. **Created Expense Model (`expenses/models.py`):**
   - Defined `Expense` class with fields: title, amount, category, date.
   - Linked to User via `ForeignKey`.

9. **Initialized Database:**
   - `python manage.py makemigrations expenses` (Prepared the database scripts).
   - `python manage.py migrate` (Created the SQLite file and Auth tables).

10. **Created Admin User:**
    - `python manage.py createsuperuser` (Tested the auth system).

## 3. Authentication & Views Implementation

11. **Configured URLs:**
    - Created `expenses/urls.py` and mapped `LoginView`, `LogoutView`.
    - Included app URLs in the main `expense_tracker/urls.py`.

12. **Auth Settings (`settings.py`):**
    - Set `LOGIN_REDIRECT_URL = 'expense-list'`.
    - Set `LOGIN_URL = 'login'` to automatically redirect unauthenticated users.

13. **Created Templates:**
    - Added `expenses/templates/expenses/login.html` with error handling.

14. **Implemented Views (`expenses/views.py`):**
    - Created `ExpenseListView` (READ): Uses `get_queryset` to ensure users only see their own data.
    - Created `ExpenseCreateView` (CREATE): Uses `form_valid` to auto-assign the logged-in user.
    - Applied `LoginRequiredMixin` to all views to restrict access.