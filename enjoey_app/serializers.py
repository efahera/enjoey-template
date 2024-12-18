from rest_framework import serializers
from .models import Staff, School

class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = '__all__'
