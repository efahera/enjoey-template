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

    branch_options = (
        ('KL', 'Kuala Lumpur'),
        ('SGR', 'Selangor'),
    )

    # Staff Table
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

    # School Table
    academyYear = models.IntegerField()
    academyMonth = models.IntegerField()
    startDate = models.DateField() #dd/mm/yyyy
    classroom_name = models.CharField(max_length=100)
    isPrimary = models.BooleanField(default=False) # TRUE/FALSE
    Branches = models.CharField(max_length=100, choices=branch_options) # make a list of branches
    IsFranchiseStaff = models.BooleanField(default=False)

class Children(models.Model):

    gender_options = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    ethnicity_options = (
        ('Chinese', 'Chinese'),
        ('Malay', 'Malay'),
        ('Indian', 'Indian'),
        ('Others', 'Others'),
    )

    religion_options = (
        ('Buddhism', 'Buddhism'),
        ('Islam', 'Islam'),
        ('Hinduism', 'Hinduism'),
        ('Christianity', 'Christianity'),
        ('Others', 'Others'),
    )

    language_options = (
        ('Chinese', 'Chinese'),
        ('Malay', 'Malay'),
        ('Tamil', 'Tamil'),
        ('English', 'English'),
        ('Others', 'Others'),
    )

    residential_options = (
        ('Citizenship', 'Citizenship'),
        ('Non-citizenship', 'Non-citizenship'),
    )

    relation_options = (
        ('FATHER', 'FATHER'),
        ('MOTHER', 'MOTHER'),
        ('UNCLE', 'UNCLE'),
        ('AUNTY', 'AUNTY'),
        ('GRANDMOTHER', 'GRANDMOTHER'),
        ('GRANDFATHER', 'GRANDFATHER'),
    )

    # Children School Table
    schoolName = models.CharField(max_length=100)
    branchName = models.CharField(max_length=100)
    programsName = models.CharField(max_length=100)
    classroomName = models.CharField(max_length=100)
    academyYear = models.IntegerField() # YYYY
    academyMonth = models.IntegerField() # MM
    enrollmentDate = models.DateField()

    # Children Table
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    birthDate = models.DateField()
    birthFutureDate = models.DateField(blank=True, null=True)
    childNRIC = models.CharField(
            max_length=14,
            validators=[
                RegexValidator(
                    regex=r'^\d{6}-\d{2}-\d{4}$',
                    message='Please use XXXXXX-XX-XXXX format.',
                    code='invalid_nric_format'
                )
            ]
        )
    birthCountry = models.CharField(max_length=100)
    profileImage = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, choices=gender_options) #	Male/Female
    age = models.IntegerField(blank=True, null=True)
    ethnicity = models.CharField(max_length=100, choices=ethnicity_options) # Chinese/Malay/Indian/Others
    religion = models.CharField(max_length=100, choices=religion_options) # Buddhism/Islam/Hinduism/Christianity/Others
    isFutureChild = models.BooleanField(default=False)
    haveSibling = models.BooleanField(default=False)
    isStaffChild = models.BooleanField(default=False)
    foreignName = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=100, choices=language_options)	# Chinese/Malay/Tamil/English/Others
    residential = models.CharField(max_length=100, choices=residential_options) #	Citizenship/Non-citizenship
    otherEthnicity = models.CharField(max_length=100, blank=True, null=True) # Mandatory ONLY IF ethnicity = OTHERS
    otherLanguage = models.CharField(max_length=100, blank=True, null=True)	# Mandatory ONLY IF language = OTHERS
    otherReligion = models.CharField(max_length=100, blank=True, null=True)	# Mandatory ONLY IF religion = OTHERS

    # Parents Table
    isSingle = models.BooleanField(default=False)
    isGuardian = models.BooleanField(default=False)
    parentFirstName = models.CharField(max_length=100)
    parentLastName = models.CharField(max_length=100)
    parentEmail = models.CharField(max_length=100)
    parentPhone = models.BigIntegerField()
    parentOccupation = models.CharField(max_length=100, blank=True, null=True)
    parentNRIC = models.CharField(
            max_length=14,
            validators=[
                RegexValidator(
                    regex=r'^\d{6}-\d{2}-\d{4}$',
                    message='Please use XXXXXX-XX-XXXX format.',
                    code='invalid_nric_format'
                )
            ]
        )
    parentBirthCountry = models.CharField(max_length=100)
    relation = models.CharField(max_length=100, choices=relation_options)
    parentAddress = models.CharField(max_length=100)
    parentCountry = models.CharField(max_length=100)
    parentPostcode = models.IntegerField()
    parentState = models.CharField(max_length=100)
    isStaff1 = models.BooleanField(default=False)
    parentFirstName2 = models.CharField(max_length=100)
    parentLastName2 = models.CharField(max_length=100)
    parentEmail2 = models.CharField(max_length=100)
    parentPhone2 = models.BigIntegerField()
    parentOccupation2 = models.CharField(max_length=100, blank=True, null=True)
    parentNRIC2 = models.CharField(
            max_length=14,
            validators=[
                RegexValidator(
                    regex=r'^\d{6}-\d{2}-\d{4}$',
                    message='Please use XXXXXX-XX-XXXX format.',
                    code='invalid_nric_format'
                )
            ]
        )
    parentBirthCountry2 = models.CharField(max_length=100)
    relation2 = models.CharField(max_length=100, choices=relation_options)
    parentAddress2 = models.CharField(max_length=100)
    parentCountry2 = models.CharField(max_length=100)
    parentPostcode2 = models.CharField(max_length=100)
    parentState2 = models.CharField(max_length=100)
    isStaff2 = models.BooleanField(default=False)

    # Finance Table
    depositAmount = models.FloatField() #	parent deposit amount to school
    depositeDate = models.DateField()
    creditAmount = models.FloatField() # If school own any amount to parents as of new academy year
    outstandingAmount = models.FloatField() # If parents own any amount to school as of new academy year
