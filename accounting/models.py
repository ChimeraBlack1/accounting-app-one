from django.db import models

# Create your models here.
class Account(models.Model):

    accountChoices = (
        ('A', 'Asset'),
        ('L', 'Liability'),
        ('E', 'Equity')
    )

    account_number = models.IntegerField(unique=True)
    account_name = models.CharField(max_length=100, unique=True)
    account_type = models.CharField(max_length=1, default="A", choices=accountChoices)
    account_balance = models.DecimalField(max_digits=25, decimal_places=2, default=0)

    def __str__(self):
        return self.account_name

class Item(models.Model):

    itemChoices = (
        ('1', 'Video Games'),
        ('2', 'Board Games'),
        ('3', 'Toys'),
    )

    item = models.CharField(max_length=50, default="New Item", choices=itemChoices)
    newItemName = models.CharField(max_length=50, default="New Item")

    def __str__(self):
        return self.newItemName





