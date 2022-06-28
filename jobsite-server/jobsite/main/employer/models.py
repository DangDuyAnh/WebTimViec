from django.db import models

class Employer(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=16, blank=True, null=True)
    image_link = models.CharField(max_length=256, blank=True, null=True)
    status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'employer'