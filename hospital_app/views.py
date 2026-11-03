from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View


class HospitalView(View):
    def get(self, request):
        data = {
            "hospital_name": "City Hospital",
            "location": "Kochi",
            "contact": "9876543210",
            "status": "Open"
        }
        return JsonResponse(data)


class DoctorView(View):
    def get(self, request):
        data = {
            "id": 1,
            "name": "Dr. Rahul",
            "specialization": "Cardiology",
            "experience": "10 Years",
            "consultation_fee": 500
        }
        return JsonResponse(data)


class PatientView(View):
    def get(self, request):
        data = {
            "id": 101,
            "name": "Anu",
            "age": 25,
            "place": "Thrissur",
            "problem": "Fever",
            "status": "Consultation Pending"
        }
        return JsonResponse(data)


class DepartmentsView(View):
    def get(self, request):
        data = {
            "departments": [
                "Cardiology",
                "Neurology",
                "Orthopedics",
                "Dermatology",
                "Pediatrics"
            ]
        }
        return JsonResponse(data)