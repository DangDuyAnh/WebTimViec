from django.db import models


class Employee(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=16, blank=True, null=True)
    image_link = models.CharField(max_length=256, blank=True, null=True)
    literacy = models.CharField(max_length=64, blank=True, null=True)
    specialist_knowledge = models.CharField(max_length=256, blank=True, null=True)
    experience = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'