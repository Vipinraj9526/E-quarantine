from django.shortcuts import render

# Create your views here.
def view(request):
    return render(request,'complaint_table/view_complaint_pol.html')

def reply(request):
    return render(request,'complaint_table/reply_complaint.html')