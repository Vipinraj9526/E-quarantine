from django.db import models

# Create your models here.
class Emergency(models.Model):
    e_id = models.AutoField(primary_key=True)
    contact_no = models.CharField(max_length=50)
    details = models.CharField(max_length=500)
    h_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'emergency'
