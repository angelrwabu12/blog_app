from django.shortcuts import render,redirect,get_object_or_404
from .models import BlogItems
from .forms import BlogForm
from .forms import NewUserFrom
from django.contrib import messages
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer



@api_view(['GET','POST'])
def blog_list(request):

    if request.method=='GET':
        blogs=BlogItems.objects.all()
        serializer=BlogSerializer(blogs,many=True)
        return Response(serializer.data)
 
    if request.method =='POST':
        serializer=BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def blog_detail(request,id):
    try:
        blog=BlogItems.objects.get(pk=id)
    except BlogItems.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serializer=BlogSerializer(blog)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer=BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors,statu=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
         blog.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)

def registration(request):
    if request.method =="POST":
        form =NewUserFrom(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request,"Registration successful.")
            return redirect('/')
        messages.error(request,"unsuccessful registration")
    form=NewUserFrom()
    return render(request=request,template_name="registration.html",context={"form":form}) 

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

def readmore(request,pk):
    blog=get_object_or_404(BlogItems,pk=pk)
    return render(request,'readmore.html',{'blog':blog})

def addblog(request):
    if request.method =='POST':
        form =BlogForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=BlogForm()
    return render(request, 'addblog.html', {'form':form})