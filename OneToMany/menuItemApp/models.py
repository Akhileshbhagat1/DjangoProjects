from django.db import models


class Menu(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)


class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=20)
    item_price = models.DecimalField(max_digits=5, decimal_places=2)
    # menu       = models.ForeignKey(menu, on_delete = models.CASCADE)

# Create your models here.
