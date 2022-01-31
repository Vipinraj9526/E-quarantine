from django.db import models

# Create your models here.
class QueryTable(models.Model):
    q_id = models.AutoField(primary_key=True)
    query = models.CharField(max_length=500)
    reply = models.CharField(max_length=500)
    time = models.TimeField()
    date = models.DateField()
    u_id = models.IntegerField()
    h_id = models.IntegerField(db_column='h-id')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'query_table'
