from django.shortcuts import render

# Create your views here.

def view(request):
    return render(request,'query_table/view_query.html')
def reply(request):
    return render(request,'query_table/reply_queries.html')