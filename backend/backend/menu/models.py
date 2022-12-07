from django.db import models

# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.IntegerField(default=10)

    def _str_(self):
        return self.title