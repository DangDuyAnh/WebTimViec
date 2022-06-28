from django.db import models

class Job(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    company = models.ForeignKey('Company', models.DO_NOTHING)
    title = models.CharField(max_length=128, blank=True, null=True)
    public_date = models.DateField(blank=True, null=True)
    expired_date = models.DateField(blank=True, null=True)
    field = models.CharField(max_length=64, blank=True, null=True)
    salary_min = models.PositiveBigIntegerField(blank=True, null=True)
    salary_max = models.PositiveBigIntegerField(blank=True, null=True)
    position = models.CharField(max_length=64, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    required_experience = models.CharField(max_length=64, blank=True, null=True)
    avaiable_slot = models.PositiveIntegerField(blank=True, null=True)
    accepted_applicant = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job'