
from django.db import models

class Transaction(models.Model):

    TRANSACTION_TYPES = [
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    ]

    title = models.CharField(max_length=100)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    category = models.CharField(max_length=50)

    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES
    )

    date = models.DateField()

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

