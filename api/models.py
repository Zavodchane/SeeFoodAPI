from django.db import models


class Dish(models.Model):
    name_dish = models.CharField(max_length=20)
    recept_dish = models.TextField()
