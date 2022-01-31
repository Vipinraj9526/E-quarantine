from django.shortcuts import render
# Create your views here.
def view_health(request):
    return render(request,"health_details/view_health_details.html")