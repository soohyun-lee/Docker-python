from django.db import models
from django.db.models.fields import CharField

class User(models.Model):
    name = models.CharField(max_length=50)
    token = models.CharField(max_length=500)
    class Meta:
        db_table = 'user'