from django.db import models
from django.core.validators import RegexValidator

class Staff(models.Model):

    gender_options = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    role_options = (
        ('Management', 'Management'),
        ('Admin', 'Admin'),
        ('Supervisor', 'Supervisor'),
        ('Account', 'Account'),
        ('Teacher', 'Teacher'),
    )

    school_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=100, choices=gender_options)
    dob = models.DateField() # dd/mm/yyyy
    profileImage = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    birthCountry = models.CharField(max_length=100)
    postcode = models.IntegerField()
    role = models.CharField(max_length=100, choices=role_options) # management/admin/supervisor/account/teacher
    isWebAccess = models.BooleanField(default=False) # TRUE/FALSE
    isMobileAccess = models.BooleanField(default=False) # TRUE/FALSE
    doj = models.DateField() #dd/mm/yyyy
    isExternal = models.BooleanField(default=False) # TRUE/FALSE
    staffNRIC = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                regex=r'^\d{6}-\d{2}-\d{4}$',
                message='Please use XXXXXX-XX-XXXX format.',
                code='invalid_nric_format'
            )
        ]
    )

class School(models.Model):

    branch_options = (
        ('KL', 'Kuala Lumpur'),
        ('SGR', 'Selangor'),
    )

    academyYear = models.IntegerField()
    academyMonth = models.IntegerField()
    startDate = models.DateField() #dd/mm/yyyy
    classroom_name = models.CharField(max_length=100)
    isPrimary = models.BooleanField(default=False) # TRUE/FALSE
    Branches = models.CharField(max_length=100, choices=branch_options) # make a list of branches
    IsFranchiseStaff = models.BooleanField(default=False)

