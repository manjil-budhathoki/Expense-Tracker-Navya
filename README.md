# Django Expense Tracker

A secure Django web app for tracking personal expenses with authentication, CRUD operations, and data filtering.

## Setup Instructions

**1. Install Dependencies**
```bash
pip install django
```

**2. Initialize Database**
*Important: Run this before starting the server to set up the Custom User Model.*
```bash
python manage.py makemigrations expenses
python manage.py migrate
```

**3. Create Admin User**
```bash
python manage.py createsuperuser
```

**4. Run Server**
```bash
python manage.py runserver
```
Access the app at: `http://127.0.0.1:8000/`

---

## 🧪 How to Test

1.  **Authentication:**
    *   Login at `/login/` (or use the **Register** link to create a new user).
    *   Unauthenticated users are automatically redirected to login.

2.  **CRUD Operations:**
    *   **Create:** Click "+ Add New Expense". (Negative amounts are blocked by validation).
    *   **Read:** View your personal expense list on the dashboard.
    *   **Update:** Click "Edit" to modify an expense.
    *   **Delete:** Click "Delete" and confirm the action.

3.  **Bonus Features:**
    *   **Filtering:** Use the dropdowns to filter by **Category** or **Date Range**.
    *   **Totals:** Observe the "Total Expenses" value updating dynamically based on filters.

---

## Explanation of Approach

*   **Custom User Model:** Implemented `expenses.CustomUser` at the start to ensure strict database integrity and scalability.
*   **Security:** Used `LoginRequiredMixin` on all views and filtered QuerySets strictly by `request.user` to prevent data leakage between users.
*   **Class-Based Views:** Utilized Django's standard `ListView`, `CreateView`, `UpdateView`, and `DeleteView` for clean, standard code.
*   **Validation:** Enforced positive amounts using `MinValueValidator` in the model.

*For a detailed step-by-step development log, please see [Summary.md](Summary.md).*