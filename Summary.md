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

## 4. CRUD Functionality (Completed)

15. **Implemented CRUD Views (`expenses/views.py`):**
    - **Create:** `ExpenseCreateView` with Date Picker widget.
    - **Read:** `ExpenseListView` showing tabular data.
    - **Update:** `ExpenseUpdateView` reusing the form logic.
    - **Delete:** `ExpenseDeleteView` with a confirmation page.

16. **Frontend Templates (`expenses/templates/expenses/`):**
    - `expense_list.html`: Displays table, success messages, and action buttons.
    - `expense_form.html`: Shared form for creating and editing.
    - `expense_confirm_delete.html`: Safety check before deletion.

## 5. Functionality & Refinements

17. **Data Validation (`expenses/models.py`):**
    - Imported `MinValueValidator` from `django.core.validators`.
    - Applied `MinValueValidator(0.01)` to the `amount` field to ensure positive values.
    - Utilized Django's default behavior to reject empty Titles or Amounts.

18. **Feature Implementation:**
    - **Filtering:** Modified `ExpenseListView` to accept a `?category=` query parameter.
    - **Case-Insensitivity:** Used `category__iexact` in the queryset to match categories regardless of capitalization (e.g., 'Food' matches 'FOOD').
    - **UI Enhancements:** Added a Filter Form dropdown in the template and a "Clear Filter" logic.

## 6. Bonus Features (Completed)

19. **User Registration System:**
    - Created `UserRegistrationForm` in `expenses/forms.py` inheriting from Django's `UserCreationForm` to correctly support the Custom User model.
    - Implemented `RegisterView` and `register.html` to allow public sign-ups without using the command line.
    - Linked registration to the Login page for seamless onboarding.

20. **Advanced Filtering & Reporting:**
    - **Date Range Filter:** Updated `get_queryset` logic in `ExpenseListView` to filter expenses by `start_date` and `end_date`.
    - **Dynamic Totals:** Implemented `get_context_data` using Django's `aggregate(Sum('amount'))` to calculate and display the total cost of currently filtered expenses.
    - **Responsive UI:** Updated `expense_list.html` with a comprehensive filter bar and a summary display box.