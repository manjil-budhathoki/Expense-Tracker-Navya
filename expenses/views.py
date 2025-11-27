from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Expense
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import ExpenseForm


# List view for expenses
class ExpenseListView(LoginRequiredMixin, ListView):

    model = Expense
    template_name = 'expenses/expense_list.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        
        # this ensue the database only fetches expenses related to logged in user
        return Expense.objects.filter(user=self.request.user).order_by('-date')

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
    