from django.shortcuts import render
from login.models import Login
# Create your views here.
def login(request):
    if request.method=="POST":
        ob=Login()
        ob.u_id="1"
        ob.l_id="1"
        ob.u_name=request.POST.get("u_name")
        ob.password=request.POST.get("Password")
        ob.type="hospital"
    return render(request,'login/login.html')