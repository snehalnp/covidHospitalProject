from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('patients/register/', views.register_patient),
    path('patients/<int:patient_id>/create_report/', views.create_report),
    path('patients/<int:patient_id>/all_reports/', views.get_all_reports),
    path('reports/<str:status>/', views.get_reports_by_status),

]