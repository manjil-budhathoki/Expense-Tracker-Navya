from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [

    # Auth Views
    path('login/', LoginView.as_view(template_name='expenses/login.html'), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),

    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Expense Views
    path('', views.ExpenseListView.as_view(), name='expense-list'),
    path('create/', views.ExpenseCreateView.as_view(), name='expense-create'),
    path('<int:pk>/edit/', views.ExpenseUpdateView.as_view(), name='expense-edit'),
    path('<int:pk>/delete/', views.ExpenseDeleteView.as_view(), name='expense-delete'),
]