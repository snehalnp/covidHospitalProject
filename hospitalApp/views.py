from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from .models import User, Patient, Report
from .serializers import UserSerializer, PatientSerializer, ReportSerializer


def home(request):
    return render(request, 'home.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # to check if user already exists
        user_obj = User.objects.filter(username = username)

        if not user_obj.exists():
            messages.warning(request, "Account does not exists")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user_obj = authenticate(username = username, password = password)
        if not user_obj:
            messages.warning(request, "Invalid Password")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        login(request, user_obj)
        return redirect('/')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # to check if user already exists
        user_obj = User.objects.filter(username = username)

        if user_obj.exists():
            messages.warning(request, "Username already exists")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if password == confirm_password:
            user = User.objects.create(username = username)
            user.set_password(password)
            user.save()
            return redirect('/')
        else:
            messages.warning(request, "Your Password does not match")

    return render(request,'register.html')


@api_view(['POST'])
def register_patient(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        patient, created = Patient.objects.get_or_create(phone_number=serializer.validated_data['phone_number'])
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_report(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    serializer = ReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(doctor=request.user, patient=patient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_reports(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    reports = Report.objects.filter(patient=patient).order_by('date')
    serializer = ReportSerializer(reports, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_reports_by_status(request, status):
    reports = Report.objects.filter(status=status)
    serializer = ReportSerializer(reports, many=True)
    return Response(serializer.data)