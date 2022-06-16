# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=256, blank=True, null=True)
    password = models.CharField(max_length=256, blank=True, null=True)
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    social_account = models.CharField(max_length=256, blank=True, null=True)
    social_account_id = models.CharField(max_length=256, blank=True, null=True)
    social_auth_iss = models.CharField(max_length=256, blank=True, null=True)
    joined_date = models.DateTimeField(blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    token_expires = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'