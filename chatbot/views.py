from django.shortcuts import render
#from . import main,long_responses

# Create your views here.
#def bot(request):
   # exec(open("main.py").read())
  #  return render(request,'chatbot.html')

def bot(request):
    return exec(open("app.py").read())
