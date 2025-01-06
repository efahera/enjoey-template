import os
import csv
from .models import Staff
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime

class UploadCSVView(APIView):

    def get(self, request, *args, **kwargs):
        return render(request, 'upload_csv_staff.html')  

    def post(self, request, *args, **kwargs):
        csv_file = request.FILES.get('csv_file')

        if csv_file:
            try:            
                success, errors = self.read_csv_file(csv_file)

                if errors:
                    error_messages = "\n".join(errors)
                    
                    print(f"Errors encountered during CSV processing:\n{error_messages}")

                    return HttpResponse(
                        f"Data uploaded contains errors:\n{error_messages}", 
                        status=400
                    )

                return HttpResponse("Successfully updated Staff and School files.")

            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        else:
            return HttpResponse("No CSV file uploaded.", status=400)

    # Read CSV file
    def read_csv_file(self, csv_file):

        file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(file)

        errors = []

        for row in reader:

            try:

            # Read Staff CSV file 
                # Staff
                schoolName = row['schoolName'].strip()
                branchName = row['branchName'].strip()
                firstName = row['firstName'].strip()
                lastName = row['lastName'].strip()
                email = row['email'].strip()
                phone = self.format_phone(row['phone'])
                gender = row['gender'].strip()
                dob = row['dob'].strip()
                dob = datetime.strptime(dob, '%d/%m/%Y').strftime('%Y-%m-%d').strip()
                profileImage = row['profileImage'].strip()
                address = row['address'].strip()
                state = row['state'].strip()
                country = row['country'].strip()
                birthCountry = row['birthCountry'].strip()
                postcode = row['postcode'].strip()
                role = row['role'].strip()
                isWebAccess = row['isWebAccess'].upper().strip()
                if isWebAccess == 'TRUE': isWebAccess = True
                elif isWebAccess == 'FALSE': isWebAccess = False
                else: raise ValueError(f"Invalid value for isWebAccess: {row['isWebAccess']}")
                isMobileAccess = row['isMobileAccess'].upper().strip()
                if isMobileAccess == 'TRUE': isMobileAccess = True
                elif isMobileAccess == 'FALSE': isMobileAccess = False
                else: raise ValueError(f"Invalid value for isMobileAccess: {row['isMobileAccess']}")
                doj = row['doj'].strip()
                doj = datetime.strptime(doj, '%d/%m/%Y').strftime('%Y-%m-%d').strip()
                isExternal = row['isExternal'].upper().strip()
                if isExternal == 'TRUE': isExternal = True
                elif isExternal == 'FALSE': isExternal = False
                else: raise ValueError(f"Invalid value for isExternal: {row['isExternal']}")
                staffNRIC = row['staffNRIC'].strip()

                # School
                academyYear = row['academyYear'].strip()
                academyMonth = row['academyMonth'].strip()
                startDate = row['startDate']
                startDate = datetime.strptime(startDate, '%d/%m/%Y').strftime('%Y-%m-%d')
                classroomName = row['classroomName'].strip()
                isPrimary = row['isPrimary'].upper().strip()
                if isPrimary == 'TRUE': isPrimary = True
                elif isPrimary == 'FALSE': isPrimary = False
                else: raise ValueError(f"Invalid value for isPrimary: {row['isPrimary']}")
                Branches = row['Branches']
                IsFranchiseStaff = row['IsFranchiseStaff'].upper().strip()
                if IsFranchiseStaff == 'TRUE': IsFranchiseStaff = True
                elif IsFranchiseStaff == 'FALSE': IsFranchiseStaff = False
                else: raise ValueError(f"Invalid value for IsFranchiseStaff: {row['IsFranchiseStaff']}")

            # Insert Staff records into database
                staff, created = Staff.objects.get_or_create(
                    email=email,
                    defaults={
                        # Staff
                        'schoolName': schoolName,
                        'branchName': branchName,
                        'firstName': firstName,
                        'lastName': lastName,
                        'phone': phone,
                        'gender': gender,
                        'dob': dob,
                        'profileImage': profileImage,
                        'address': address,
                        'state': state,
                        'country': country,
                        'birthCountry': birthCountry,
                        'postcode': postcode,
                        'role': role,
                        'isWebAccess': isWebAccess,
                        'isMobileAccess': isMobileAccess,
                        'doj': doj,
                        'isExternal': isExternal,
                        'staffNRIC': staffNRIC,

                        # School
                        'academyYear': academyYear,
                        'academyMonth': academyMonth,
                        'startDate': startDate,
                        'classroomName': classroomName,
                        'isPrimary': isPrimary,
                        'Branches': Branches,
                        'IsFranchiseStaff': IsFranchiseStaff,
                    }
                )             

            except ValueError as e:
                error_message = f"Row {reader.line_num}: Error parsing date or other field: {e}"
                errors.append(error_message)
                print(error_message)
            except KeyError as e:
                error_message = f"Row {reader.line_num}: Missing field {e}"
                errors.append(error_message)
                print(error_message)
            except Exception as e:
                error_message = f"Row {reader.line_num}: Unexpected error: {e}"
                errors.append(error_message)
                print(error_message)

        return (True if not errors else False), errors

    # Format phone number
    def format_phone(self, phone): 
        if phone:
            if phone[0] == '1':
                phone = phone.replace("-", "")
                return '60' + phone

            elif phone[0] == '0':
                phone = phone.replace("-", "")
                return '6' + phone

            return phone

        return ''
