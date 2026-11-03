from django.urls import path
from hospital_app import views

urlpatterns = [
    path('hospital/', views.HospitalView.as_view()),
    path('doctor/', views.DoctorView.as_view()),
    path('patient/', views.PatientView.as_view()),
    path('departments/', views.DepartmentsView.as_view()),
]