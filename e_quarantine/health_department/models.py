from django.db import models

# Create your models here.
class HealthDepartment(models.Model):
    h_id = models.AutoField(primary_key=True)
    h_department = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    landline = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'health_department'
