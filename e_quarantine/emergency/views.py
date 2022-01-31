from django.shortcuts import render
from emergency.models import Emergency
# Create your views here.

def add(request):
    if request.method=="POST":
        ob=Emergency()
        ob.contact_no=request.POST.get('number')
        ob.details=request.POST.get('details')
        ob.h_id="1"
        ob.save()
    return render(request,'emergency/add_contact.html')