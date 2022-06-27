from django.db import models

class Company(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    province = models.ForeignKey('Province', models.DO_NOTHING)
    desc = models.CharField(max_length=256)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company'