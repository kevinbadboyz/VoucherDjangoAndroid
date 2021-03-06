from django.db import models

class Game(models.Model):
    name = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
