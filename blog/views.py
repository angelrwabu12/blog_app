from django.shortcuts import render
from .models import BlogItems

def home(request):
    blogs =BlogItems.objects.all()
    context={"blogs":blogs}
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def readmore(request):
    return render(request,'readmore.html')
def addblog(request):
    return render(request,'addblog.html')