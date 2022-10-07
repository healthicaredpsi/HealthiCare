from django.shortcuts import render

# Create your views here.
def pagerequest(request):
    return render(request,'relax-everything.html')