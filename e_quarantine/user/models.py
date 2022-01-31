from django.db import models

# Create your models here.
class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob = models.DateField()
    phone = models.CharField(max_length=50)
    gmail = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date = models.DateField()
    logitude = models.CharField(max_length=50)
    lattitude = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    id_proof = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user'
