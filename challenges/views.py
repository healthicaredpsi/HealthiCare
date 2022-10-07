from django.shortcuts import render

# Create your views here.
def challenges(request):
    return render(request,'challenge-everything.html')

def colorista(request):
    return render(request,'colorista-everything.html')

