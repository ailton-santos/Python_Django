from django.db import models
from django.contrib.auth.models import User

class CalorieEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    calories = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.calories} cal"