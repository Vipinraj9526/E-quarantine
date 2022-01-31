from django.shortcuts import render

# Create your views here.
def view_hospital(request):
    return render(request,'user/view_user_hos.html')
def view_police(request):
    return render(request,'user/view_user_police.html')
