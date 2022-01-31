from django.db import models

# Create your models here.
class ComplaintTable(models.Model):
    c_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    reply = models.CharField(max_length=500)
    u_id = models.IntegerField()
    p_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'complaint_table'
