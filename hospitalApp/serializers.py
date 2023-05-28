from rest_framework import serializers
from .models import User, Patient, Report

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['phone_number']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['doctor', 'patient', 'status', 'date']
