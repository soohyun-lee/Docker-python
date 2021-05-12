from django.db import models
from django.db.models.fields.related import ForeignKey
from user.models import User

class Listup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    study_date = models.CharField(max_length=100,null=True)
    title = models.CharField(max_length=100, null=True)
    study_contents = models.CharField(max_length=500, null=True) 
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'contents'
     