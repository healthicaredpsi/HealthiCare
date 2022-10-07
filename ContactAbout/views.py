from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,'contact-everything.html')

def about_before_login(request):
    return render(request,'about-everything_1.html')

def about_after_login(request):
    return render(request,'about-everything_2.html')