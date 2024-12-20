import os
import csv
from .models import Staff, School
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
                self.read_csv_file(csv_file)
                return HttpResponse("Successfully updated Staff and School files.")

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
            # Read Staff CSV file by row
                school_name = row['school_name']
                branch_name = row['branch_name']
                firstName = row['firstName']
                lastName = row['lastName']
                email = row['email']
                phone = row['phone']
                gender = row['gender']
                dob = row['dob']
                dob = datetime.strptime(dob, '%d/%m/%Y').strftime('%Y-%m-%d')
                profileImage = row['profileImage']
                address = row['address']
                state = row['state']
                country = row['country']
                birthCountry = row['birthCountry']
                postcode = row['postcode']
                role = row['role']
                isWebAccess = row['isWebAccess'].upper() # changed any values to uppercase
                if isWebAccess == 'TRUE': isWebAccess = True
                elif isWebAccess == 'FALSE': isWebAccess = False
                else: raise ValueError(f"Invalid value for isWebAccess: {row['isWebAccess']}")
                isMobileAccess = row['isMobileAccess'].upper()
                if isMobileAccess == 'TRUE': isMobileAccess = True
                elif isMobileAccess == 'FALSE': isMobileAccess = False
                else: raise ValueError(f"Invalid value for isMobileAccess: {row['isMobileAccess']}")
                doj = row['doj']
                doj = datetime.strptime(doj, '%d/%m/%Y').strftime('%Y-%m-%d')
                isExternal = row['isExternal'].upper()
                if isExternal == 'TRUE': isExternal = True
                elif isExternal == 'FALSE': isExternal = False
                else: raise ValueError(f"Invalid value for isExternal: {row['isExternal']}")
                staffNRIC = row['staffNRIC']

            # Insert Staff records to database
                staff, created = Staff.objects.get_or_create(
                    email=email,
                    defaults={
                        'school_name': school_name,
                        'branch_name': branch_name,
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
                    }
                )             

            # Read School CSV file by row
                academyYear = row['academyYear']
                academyMonth = row['academyMonth']
                start_date = row['startDate']
                start_date = datetime.strptime(start_date, '%d/%m/%Y').strftime('%Y-%m-%d')
                classroom_name = row['classroom_name']
                isPrimary = row['isPrimary'].strip().upper() == 'TRUE'
                Branches = row['Branches']
                IsFranchiseStaff = row['IsFranchiseStaff'].strip().upper() == 'TRUE'
        
            # Insert School records to database
                school, created = School.objects.update_or_create(
                    academyYear=row['academyYear'], 
                    defaults={
                        'academyMonth': academyMonth,
                        'startDate': start_date,
                        'classroom_name': classroom_name,
                        'isPrimary': isPrimary,
                        'Branches': Branches,
                        'IsFranchiseStaff': IsFranchiseStaff,
                    }
                ) 

            except ValueError as e:
                print(f"Error parsing date or other field: {e}")
                continue

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
