from django.shortcuts import render
from health_department.models import HealthDepartment
# Create your views here.

def register(request):
    if request.method=="POST":
        ob=HealthDepartment()
        ob.h_department=request.POST.get("h_name")
        ob.address=request.POST.get("address")
        ob.landline=request.POST.get("landline")
        ob.email=request.POST.get("email")
        ob.password=request.POST.get("password")
        ob.save()
    return render(request,'health_department/Register_hospital.html')