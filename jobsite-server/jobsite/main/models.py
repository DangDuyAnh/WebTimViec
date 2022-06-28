from django.db import models


class Province(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=64)
    area_code = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'province'
