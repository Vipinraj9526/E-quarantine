from django.db import models

# Create your models here.
class HealthDetails(models.Model):
    hd_id = models.AutoField(primary_key=True)
    temperature = models.CharField(max_length=50)
    oxygen_level = models.CharField(max_length=50)
    sugar = models.CharField(max_length=50)
    heart_rate = models.CharField(max_length=50)
    bp = models.CharField(max_length=50)
    u_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'health_details'
