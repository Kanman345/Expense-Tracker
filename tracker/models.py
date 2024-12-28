from django.db import models

# Create your models here.

class Budget(models.Model):
    name = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    
    
    def __str__(self):
        return self.name

class Transaction(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=100)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.description} - {self.amount} ({self.budget.name})"