from django import forms
from .models import Patient,Report


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['Phone Number']


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['Doctor','Patient','Status','Date']
