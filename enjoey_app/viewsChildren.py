import os
import csv
from .models import Children
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime

class UploadCSVViewChildren(APIView):

    def get(self, request, *args, **kwargs):
        return render(request, 'upload_csv_children.html')  

    def post(self, request, *args, **kwargs):
        csv_file = request.FILES.get('csv_file')

        if csv_file:
            try:            
                self.read_csv_file(csv_file)
                return HttpResponse("Successfully updated School, Children, Parents, and Finance files.")

            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        else:
            return HttpResponse("No CSV file uploaded.", status=400)

    # Read CSV file
    def read_csv_file(self, csv_file):

        file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(file)

        for row in reader:

            try:

            # Read Children CSV file
                # Children School
                schoolName = row['schoolName']
                branchName = row['branchName']
                programsName = row['programsName']
                classroomName = row['classroomName']
                academyYear = row['academyYear']
                academyMonth = row['academyMonth']
                enrollmentDate = row['enrollmentDate']
                enrollmentDate = datetime.strptime(enrollmentDate, '%d/%m/%Y').strftime('%Y-%m-%d')

                # Children 
                firstName = row['firstName']
                lastName = row['lastName']
                birthDate = row['birthDate'] # date
                birthDate = datetime.strptime(birthDate, '%d/%m/%Y').strftime('%Y-%m-%d')
                birthFutureDate = row['birthFutureDate'] # date
                if birthFutureDate.strip():  
                    birthFutureDate = datetime.strptime(birthFutureDate.strip(), '%d/%m/%Y').strftime('%Y-%m-%d')
                else:
                    birthFutureDate = None
                childNRIC = row['childNRIC']
                birthCountry = row['birthCountry']
                profileImage = row['profileImage']
                gender = row['gender']
                age = row['age']
                ethnicity = row['ethnicity']
                religion = row['religion']
                isFutureChild = row['isFutureChild'] # boolean
                if isFutureChild == 'TRUE': isFutureChild = True
                elif isFutureChild == 'FALSE': isFutureChild = False
                else: raise ValueError(f"Invalid value for isFutureChild: {row['isFutureChild']}")
                haveSibling = row['haveSibling'] # boolean
                if haveSibling == 'TRUE': haveSibling = True
                elif haveSibling == 'FALSE': haveSibling = False
                else: raise ValueError(f"Invalid value for haveSibling: {row['haveSibling']}")
                isStaffChild = row['isStaffChild'] # boolean
                if isStaffChild == 'TRUE': isStaffChild = True
                elif isStaffChild == 'FALSE': isStaffChild = False
                else: raise ValueError(f"Invalid value for isStaffChild: {row['isStaffChild']}")
                foreignName = row['foreignName']
                language = row['language']
                residential = row['residential']
                otherEthnicity = row['otherEthnicity']
                otherLanguage = row['otherLanguage']
                otherReligion = row['otherReligion']

                # Parents 
                isSingle = row['isSingle'].upper() # boolean
                if isSingle == 'TRUE': isSingle = True
                elif isSingle == 'FALSE': isSingle = False
                else: raise ValueError(f"Invalid value for isSingle: {row['isSingle']}")
                isGuardian = row['isGuardian'].upper()  # boolean
                if isGuardian == 'TRUE': isGuardian = True
                elif isGuardian == 'FALSE': isGuardian = False
                else: raise ValueError(f"Invalid value for isGuardian: {row['isGuardian']}")
                parentFirstName = row['parentFirstName']
                parentLastName = row['parentLastName']
                parentEmail = row['parentEmail']
                parentPhone = row['parentPhone']
                parentOccupation = row['parentOccupation']
                parentNRIC = row['parentNRIC']
                parentBirthCountry = row['parentBirthCountry']
                relation = row['relation'].upper()
                parentAddress = row['parentAddress']
                parentCountry = row['parentCountry']
                parentPostcode = row['parentPostcode']
                parentState = row['parentState']
                isStaff1 = row['isStaff1'].upper()  # boolean
                if isStaff1 == 'TRUE': isStaff1 = True
                elif isStaff1 == 'FALSE': isStaff1 = False
                else: raise ValueError(f"Invalid value for isStaff1: {row['isStaff1']}")
                parentFirstName2 = row['parentFirstName2']
                parentLastName2 = row['parentLastName2']
                parentEmail2 = row['parentEmail2']
                parentPhone2 = row['parentPhone2']
                parentOccupation2 = row['parentOccupation2']
                parentNRIC2 = row['parentNRIC2']
                parentBirthCountry2 = row['parentBirthCountry2']
                relation2 = row['relation2'].upper()
                parentAddress2 = row['parentAddress2']
                parentCountry2 = row['parentCountry2']
                parentPostcode2 = row['parentPostcode2']
                parentState2 = row['parentState2']
                isStaff2 = row['isStaff2'].upper()  # boolean
                if isStaff2 == 'TRUE': isStaff2 = True
                elif isStaff2 == 'FALSE': isStaff2 = False
                else: raise ValueError(f"Invalid value for isStaff2: {row['isStaff2']}")

                # Finance
                depositAmount = row['depositAmount']
                depositeDate = row['depositeDate'] # date
                depositeDate = datetime.strptime(depositeDate, '%d/%m/%Y').strftime('%Y-%m-%d')
                creditAmount = row['creditAmount']
                outstandingAmount = row['outstandingAmount']

            # Insert Children records into database
                children, created = Children.objects.get_or_create(
                    childNRIC=childNRIC,
                    defaults={
                        # Children School
                        'schoolName': schoolName,
                        'branchName': branchName,
                        'programsName': programsName,
                        'classroomName': classroomName,
                        'academyYear': academyYear,
                        'academyMonth': academyMonth,
                        'enrollmentDate': enrollmentDate,

                        # Children
                        'firstName': firstName,
                        'lastName': lastName,
                        'birthDate': birthDate,
                        'birthFutureDate': birthFutureDate,
                        'birthCountry': birthCountry,
                        'profileImage': profileImage,
                        'gender': gender,
                        'age': age,
                        'ethnicity': ethnicity,
                        'religion': religion,
                        'isFutureChild': isFutureChild,
                        'haveSibling': haveSibling,
                        'isStaffChild': isStaffChild,
                        'foreignName': foreignName,
                        'language': language,
                        'residential': residential,
                        'otherEthnicity': otherEthnicity,
                        'otherLanguage': otherLanguage,
                        'otherReligion': otherReligion,

                        # Parents
                        'isSingle': isSingle,
                        'isGuardian': isGuardian,
                        'parentFirstName': parentFirstName,
                        'parentLastName': parentLastName,
                        'parentEmail': parentEmail,
                        'parentPhone': parentPhone,
                        'parentOccupation': parentOccupation,
                        'parentNRIC': parentNRIC,
                        'parentBirthCountry': parentBirthCountry,
                        'relation': relation,
                        'parentAddress': parentAddress,
                        'parentCountry': parentCountry,
                        'parentPostcode': parentPostcode,
                        'parentState': parentState,
                        'isStaff1': isStaff1,
                        'parentFirstName2': parentFirstName2,
                        'parentLastName2': parentLastName2,
                        'parentEmail2': parentEmail2,
                        'parentPhone2': parentPhone2,
                        'parentOccupation2': parentOccupation2,
                        'parentNRIC2': parentNRIC2,
                        'parentBirthCountry2': parentBirthCountry2,
                        'relation2': relation2,
                        'parentAddress2': parentAddress2,
                        'parentCountry2': parentCountry2,
                        'parentPostcode2': parentPostcode2,
                        'parentState2': parentState2,
                        'isStaff2': isStaff2,

                        # Finance
                        'depositAmount': depositAmount,
                        'depositeDate': depositeDate,
                        'creditAmount': creditAmount,
                        'outstandingAmount': outstandingAmount,


                    }
                )

            except ValueError as e:
                print(f"Error parsing date or other field: {e}")
                continue
