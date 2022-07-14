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
    main_cv_id = models.BigIntegerField(blank=True, null=True)
    main_letter_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class EmployeeAppliedJob(models.Model):
    employee = models.OneToOneField('Employee', models.DO_NOTHING, primary_key=True)
    job = models.ForeignKey('Job', models.DO_NOTHING)
    status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'employee_applied_job'
        unique_together = (('employee', 'job'),)


class EmployeeSavedJob(models.Model):
    employee = models.OneToOneField('Employee', models.DO_NOTHING, primary_key=True)
    job = models.ForeignKey('Job', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee_saved_job'
        unique_together = (('employee', 'job'),)


class EmployeeCv(models.Model):
    employee = models.OneToOneField('Employee', models.DO_NOTHING, primary_key=True)
    cv_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'employee_cv'
        unique_together = (('employee', 'cv_id'),)


class EmployeeLetter(models.Model):
    employee = models.OneToOneField('Employee', models.DO_NOTHING, primary_key=True)
    letter_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'employee_letter_cv'
        unique_together = (('employee', 'letter_cv_id'),)