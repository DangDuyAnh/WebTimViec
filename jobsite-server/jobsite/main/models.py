from django.db import models

# Create your models here.
""" class User(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=256, blank=True, null=True)
    password = models.CharField(max_length=256, blank=True, null=True)
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    social_account = models.CharField(max_length=256, blank=True, null=True)
    social_account_id = models.BigIntegerField(blank=True, null=True)
    social_auth_iss = models.CharField(max_length=256, blank=True, null=True)
    joined_date = models.DateTimeField(blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    token_expires = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user' """
