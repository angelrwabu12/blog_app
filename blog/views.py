from django.shortcuts import render
from .models import BlogItems

def home(request):
    blog=BlogItems.objects.all()
    context={"BlogItems":blog}
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')