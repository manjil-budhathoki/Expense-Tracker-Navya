from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [

    # Auth Views
    path('login/', LoginView.as_view(template_name='expenses/login.html'), name='login'),

    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Expense Views
    path('', views.ExpenseListView.as_view(), name='expense-list'),
    path('create/', views.ExpenseCreateView.as_view(), name='expense-create'),
]