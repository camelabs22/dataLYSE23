from django.db import models

class Users(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 200)
    password = models.CharField(max_length = 200)
    class Meta:
        db_table = "registration"
    
class User_datasets(models.Model):
    email = models.EmailField(max_length = 200)
    datasets = models.FileField(max_length=500)
    class Meta:
        db_table = 'datasets'
