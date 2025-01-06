from django.db import models
from django.core.validators import RegexValidator

class Staff(models.Model): # StaffTemp

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
    schoolName = models.CharField(max_length=100)
    branchName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=100, choices=gender_options)
    dob = models.DateField()
    profileImage = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    birthCountry = models.CharField(max_length=100)
    postcode = models.IntegerField()
    role = models.CharField(max_length=100, choices=role_options)
    isWebAccess = models.BooleanField(default=False)
    isMobileAccess = models.BooleanField(default=False)
    doj = models.DateField()
    isExternal = models.BooleanField(default=False)
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
    startDate = models.DateField()
    classroomName = models.CharField(max_length=100)
    isPrimary = models.BooleanField(default=False)
    Branches = models.CharField(max_length=100, choices=branch_options)
    IsFranchiseStaff = models.BooleanField(default=False)

class Children(models.Model): # ChildrenTemp

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
    gender = models.CharField(max_length=100, choices=gender_options)
    age = models.IntegerField(blank=True, null=True)
    ethnicity = models.CharField(max_length=100, choices=ethnicity_options)
    religion = models.CharField(max_length=100, choices=religion_options)
    isFutureChild = models.BooleanField(default=False)
    haveSibling = models.BooleanField(default=False)
    isStaffChild = models.BooleanField(default=False)
    foreignName = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=100, choices=language_options)
    residential = models.CharField(max_length=100, choices=residential_options)
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
    depositAmount = models.FloatField()
    depositeDate = models.DateField()
    creditAmount = models.FloatField()
    outstandingAmount = models.FloatField()

# class BaseModel(models.Model):
#     createdAt = models.DateTimeField(auto_now_add=True)
#     updatedAt = models.DateTimeField(auto_now=True)
    
#     class Meta:
#         abstract = True

# class Tenant(models.Model):
#     name = models.CharField(max_length=250)

# class Branch(BaseModel):
#     tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
#     name = models.CharField(max_length=250)
#     type = models.CharField(max_length=2, choices=BRANCH_TYPE, default='1')
#     image = models.ImageField(storage=TenantStorage(), null=True)
#     email = models.EmailField(null=True)
#     isMainBranch = models.BooleanField(default=False)
#     startMonth = models.CharField(max_length=4)
#     EndMonth = models.CharField(max_length=4)
#     address = models.CharField(max_length=250, null=True)
#     state = models.CharField(max_length=50, null=True)
#     country = models.CharField(max_length=100, null=True)
#     postcode = models.CharField(max_length=10, null=True)
#     phone = models.CharField(max_length=20, null=True)
#     isActive = models.BooleanField(default=False)
#     isArchived = models.BooleanField(default=False)
#     creator = models.CharField(max_length=250)
    
#     def save(self, *args, **kwargs):
#         if self.image:
#             file_ext = os.path.splitext(str(self.image.name))[-1]
#             self.image.name = f"{self.name}_branch{file_ext}"
#             self.image.storage.bucket_name = settings.APP_PUBLIC_MEDIA_S3_BUCKET_NAME
#             self.image.storage.location = f"{self.tenant.id}/branch/avatar"
#             # self.logo.storage.bucket_name = settings.APP_MEDIA_S3_BUCKET_NAME
#             # self.logo.storage.location = "family/avatar"
    
#         super(Branch, self).save(*args, **kwargs)

# class Programs(models.Model):
#     tenantId = models.CharField(max_length=250)
#     branchId = models.BigIntegerField() # Fetch from Branch table
#     name = models.CharField(max_length=250)
#     description = models.CharField(max_length=250)
#     startingYear = models.IntegerField(blank=True)
#     startingMonth = models.IntegerField(blank=True)
#     maxYear = models.IntegerField(blank=True)
#     maxMonth = models.IntegerField(blank=True)
#     rankMonth = models.IntegerField(blank=True)
#     baseStaff = models.IntegerField(blank=True)
#     baseStudent = models.IntegerField(blank=True)
#     active = models.BooleanField(default=True)
#     isArchived = models.BooleanField(default=False)
#     isSpecial = models.BooleanField(default=False)
#     creator = models.CharField(max_length=250, editable=True)
#     createdAt = models.DateTimeField(editable=False)
#     updatedAt = models.DateTimeField()
    
#     def save(self, *args, **kwargs):
#      ''' On save, update timestamps '''
    
#         if not self.id:
#             self.createdAt = timezone.now()
#             self.updatedAt = timezone.now()
    
#         return super(Programs, self).save(*args, **kwargs)

# class ClassRooms(BaseModel):
#     tenantId = models.CharField(max_length=250)
#     branchId = models.BigIntegerField() # Fetch from Branch table
#     programs = models.ForeignKey(Programs, on_delete=models.CASCADE)
#     name = models.CharField(max_length=250)
#     maxCapacity = models.IntegerField()
#     availableCapacity = models.IntegerField()
#     academyYear = models.CharField(max_length=4)
#     isSpecial = models.BooleanField(default=False)
#     active = models.BooleanField()
#     isArchived = models.BooleanField(default=False)
#     enteredBy = models.CharField(max_length=250, editable=True)

# class Staff(BaseModel):
#     tenantId = models.CharField(max_length=250)
#     branchId = models.BigIntegerField() # Fetch from Branch table
#     firstName = models.CharField(max_length=250)
#     lastName = models.CharField(max_length=250)
#     email = models.EmailField(db_index=True, unique=True, max_length=254)
#     phone = models.CharField(max_length=50)
#     gender = models.CharField(max_length=10)
#     dob = models.CharField(max_length=10)
#     profileImage = models.FileField(storage=AvatarStorage(), null=True)
#     address = models.CharField(max_length=500, null=True)
#     state = models.CharField(max_length=50, null=True)
#     country = models.CharField(max_length=50, null=True)
#     birthCountry = models.CharField(max_length=100, null=True)
#     postcode = models.CharField(max_length=10, null=True)
#     role = models.CharField(max_length=20)
#     isWebAccess = models.BooleanField(default=False)
#     isMobileAccess = models.BooleanField(default=False)
#     doj = models.DateField()
#     isExternal = models.BooleanField(default=False)
#     userId = models.UUIDField(null=True)                            # added new
#     isActive = models.BooleanField(default=False)                   # added new
#     isPresentToday = models.BooleanField(default=False)             # added new
#     isInToday = models.BooleanField(default=False)                  # added new
#     isOutToday = models.BooleanField(default=False)                 # added new
#     staffNRIC = models.CharField(max_length=20, null=True)
#     creator = models.CharField(max_length=250, editable=False)      # added new
#     isMarkedWithdraw = models.BooleanField(default=False)           # added new
#     withDrawDate = models.CharField(max_length=10, null=True)       # added new
#     withDrawReason = models.CharField(max_length=200, null=True)    # added new
#     isArchived = models.BooleanField(default=False)                 # added new
    
#     def save(self, *args, **kwargs):
#         if self.profileImage:
#             file_ext = os.path.splitext(str(self.profileImage.name))[-1]
#             self.profileImage.name = f"{self.firstName}_{self.lastName}_avatar{file_ext}"
#             self.profileImage.storage.bucket_name = “APP_PUBLIC_MEDIA_S3_BUCKET_NAME”
#             self.profileImage.storage.location = f"{self.tenantId}/avatar/staff"
#             # self.profileImage.storage.location = "staff/avatar"
#             self.email = self.email.lower().strip()
            
#         super(Staff, self).save(*args, **kwargs)

# class Classroom_staff(models.Model):
#     tenantId = models.CharField(max_length=250)
#     branchId = models.BigIntegerField()
#     classroom = models.ForeignKey(ClassRooms, on_delete=models.CASCADE)
#     userId = models.CharField(max_length=250, null=True)
#     staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
#     assignedBy = models.CharField(max_length=250)
#     isPrimary = models.BooleanField(default=False)
#     isActive = models.BooleanField(default=False)
#     academyYear = models.CharField(max_length=4, null=True)
#     academyMonth = models.CharField(max_length=2, null=True)
#     startDate = models.DateField(null=True)
#     endDate = models.DateField(null=True)
#     isMarkedWithdraw = models.BooleanField(default=False)
#     withDrawDate = models.CharField(max_length=10, null=True)
#     withDrawReason = models.CharField(max_length=200, null=True)
#     isMarkedTransfer = models.BooleanField(default=False)
#     TransferDate = models.CharField(max_length=10, null=True)
#     TransferReason = models.CharField(max_length=200, null=True)
#     createdAt = models.DateTimeField(editable=False)
#     updatedAt = models.DateTimeField()
    
#     def save(self, *args, **kwargs):
#     ''' On save, update timestamps '''
#     if not self.id:
#         self.createdAt = timezone.now()
#         self.updatedAt = timezone.now()
#     return super(Classroom_staff, self).save(*args, **kwargs)
