import email
from sqlite3 import Timestamp
from django.db import models

# Create your models here.


class Join(models.Model):
    email = models.EmailField()
    Timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
