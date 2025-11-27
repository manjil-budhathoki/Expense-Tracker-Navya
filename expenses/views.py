from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Expense
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import ExpenseForm, UserRegistrationForm
from django.db.models import Sum



# List view for expenses
class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'expenses/expense_list.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        queryset = Expense.objects.filter(user=self.request.user).order_by('-date')
        

        # Filter by category
        category = self.request.GET.get('category')
        
        if category:
            queryset = queryset.filter(category__iexact=category)
        
        # Filter by date range
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')

        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Calculate total amount
        total = context['expenses'].aggregate(Sum('amount'))['amount__sum']
        context['total_amount'] = total if total else 0
        return context


# Create View for expenses

class ExpenseCreateView(LoginRequiredMixin, CreateView):

    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/expense_form.html'
    success_url = reverse_lazy('expense-list')


    # Assign the logged in user as the expense owner
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Expense added successfully!")
        return super().form_valid(form)

class ExpenseUpdateView(LoginRequiredMixin, UpdateView):

    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/expense_form.html'
    success_url = reverse_lazy('expense-list')


    def get_queryset(self):
        
        # allow to edit only if it's their own expense
        return Expense.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        
        messages.success(self.request, "Expense updated successfully!")
        return super().form_valid(form)

class ExpenseDeleteView(LoginRequiredMixin, DeleteView):

    model = Expense
    template_name = 'expenses/expense_confirm_delete.html'
    success_url = reverse_lazy('expense-list')

    def get_queryset(self):

        # allow to delete only if it's their own expense
        return Expense.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Expense deleted successfully!")
        return super().delete(request, *args, **kwargs)
    
class RegisterView(CreateView):

    form_class = UserRegistrationForm
    template_name = 'expenses/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Registration successful! You can now log in.")
        return super().form_valid(form)