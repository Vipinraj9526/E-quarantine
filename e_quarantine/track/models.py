from django.db import models

# Create your models here.
class Track(models.Model):
    t_id = models.AutoField(primary_key=True)
    u_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'track'