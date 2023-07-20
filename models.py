from django.db import models

# Create your models here.
class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    # Add more fields as per your requirements
