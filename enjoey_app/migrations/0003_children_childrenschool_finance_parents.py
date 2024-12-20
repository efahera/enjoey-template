# Generated by Django 5.1.4 on 2024-12-20 01:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enjoey_app', '0002_alter_staff_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('birthDate', models.DateField()),
                ('birthFutureDate', models.DateField(blank=True, null=True)),
                ('childNRIC', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(code='invalid_nric_format', message='Please use XXXXXX-XX-XXXX format.', regex='^\\d{6}-\\d{2}-\\d{4}$')])),
                ('birthCountry', models.CharField(max_length=100)),
                ('profileImage', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('ethnicity', models.CharField(choices=[('Chinese', 'Chinese'), ('Malay', 'Malay'), ('Indian', 'Indian'), ('Others', 'Others')], max_length=100)),
                ('religion', models.CharField(choices=[('Buddhism', 'Buddhism'), ('Islam', 'Islam'), ('Hinduism', 'Hinduism'), ('Christianity', 'Christianity'), ('Others', 'Others')], max_length=100)),
                ('isFutureChild', models.BooleanField(default=False)),
                ('haveSibling', models.BooleanField(default=False)),
                ('isStaffChild', models.BooleanField(default=False)),
                ('foreignName', models.CharField(blank=True, max_length=100, null=True)),
                ('language', models.CharField(choices=[('Chinese', 'Chinese'), ('Malay', 'Malay'), ('Tamil', 'Tamil'), ('English', 'English'), ('Others', 'Others')], max_length=100)),
                ('residential', models.CharField(choices=[('Citizenship', 'Citizenship'), ('Non-citizenship', 'Non-citizenship')], max_length=100)),
                ('otherEthnicity', models.CharField(blank=True, max_length=100, null=True)),
                ('otherLanguage', models.CharField(blank=True, max_length=100, null=True)),
                ('otherReligion', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChildrenSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolName', models.CharField(max_length=100)),
                ('branchName', models.CharField(max_length=100)),
                ('programsName', models.CharField(max_length=100)),
                ('classroomName', models.CharField(max_length=100)),
                ('academyYear', models.IntegerField(max_length=4)),
                ('academyMonth', models.IntegerField(max_length=2)),
                ('enrollmentDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depositAmount', models.FloatField()),
                ('depositeDate', models.DateField()),
                ('creditAmount', models.FloatField()),
                ('outstandingAmount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isSingle', models.BooleanField(default=False)),
                ('isGuardian', models.BooleanField(default=False)),
                ('parentFirstName', models.CharField(max_length=100)),
                ('parentLastName', models.CharField(max_length=100)),
                ('parentEmail', models.CharField(max_length=100)),
                ('parentPhone', models.IntegerField()),
                ('parentOccupation', models.CharField(blank=True, max_length=100, null=True)),
                ('parentNRIC', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(code='invalid_nric_format', message='Please use XXXXXX-XX-XXXX format.', regex='^\\d{6}-\\d{2}-\\d{4}$')])),
                ('parentBirthCountry', models.CharField(max_length=100)),
                ('relation', models.CharField(choices=[('FATHER', 'FATHER'), ('MOTHER', 'MOTHER'), ('UNCLE', 'UNCLE'), ('AUNTY', 'AUNTY'), ('GRANDMOTHER', 'GRANDMOTHER'), ('GRANDFATHER', 'GRANDFATHER')], max_length=100)),
                ('parentAddress', models.CharField(max_length=100)),
                ('parentCountry', models.CharField(max_length=100)),
                ('parentPostcode', models.IntegerField()),
                ('parentState', models.CharField(max_length=100)),
                ('isStaff1', models.BooleanField(default=False)),
                ('parentFirstName2', models.CharField(max_length=100)),
                ('parentLastName2', models.CharField(max_length=100)),
                ('parentEmail2', models.CharField(max_length=100)),
                ('parentPhone2', models.IntegerField()),
                ('parentOccupation2', models.CharField(blank=True, max_length=100, null=True)),
                ('parentNRIC2', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(code='invalid_nric_format', message='Please use XXXXXX-XX-XXXX format.', regex='^\\d{6}-\\d{2}-\\d{4}$')])),
                ('parentBirthCountry2', models.CharField(max_length=100)),
                ('relation2', models.CharField(choices=[('FATHER', 'FATHER'), ('MOTHER', 'MOTHER'), ('UNCLE', 'UNCLE'), ('AUNTY', 'AUNTY'), ('GRANDMOTHER', 'GRANDMOTHER'), ('GRANDFATHER', 'GRANDFATHER')], max_length=100)),
                ('parentAddress2', models.CharField(max_length=100)),
                ('parentCountry2', models.CharField(max_length=100)),
                ('parentPostcode2', models.CharField(max_length=100)),
                ('parentState2', models.CharField(max_length=100)),
                ('isStaff2', models.BooleanField(default=False)),
            ],
        ),
    ]
