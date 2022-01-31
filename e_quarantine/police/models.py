from django.db import models

# Create your models here.
class Police(models.Model):
    police = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    landline = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'police'
