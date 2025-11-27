from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


# our Custom user
class CustomUser(AbstractUser):

    pass

# Expense model
class Expense(models.Model):

    # predifined categories

    CATEGORY_CHOICES = [
        ('FOOD', 'Food'),
        ('TRAVEL', 'Travel'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('UTILITIES', 'Utilities'),
        ('OTHER', 'Other'),
    ]

    title = models.CharField(max_length=200)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.amount}" 

