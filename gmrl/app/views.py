from django.shortcuts import render,redirect
from . models import *
from django.core.exceptions import ValidationError
def index(request):
    context={}
    
    obj=Packages.objects.all()
    context['obj']=obj
    if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          message=request.POST.get('message')
          
          if request.POST:
               details=Enquiry.objects.create(name=name,email=email,phone=phone,message=message)
               details.save()
               return redirect('index')

    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')
def packages(request):
    context={}
    # obj=Subpackage.objects.filter(package=ob)

    obj=Packages.objects.all()
    context['obj']=obj
    return render(request,'packages.html',context)
def test(request):
    return render(request,'test.html')
def gallery(request):
    context={}
    o=Gallery.objects.all()
    context['o']=o
    return render(request,'gallery.html',context)
def department(request):
    return render(request,'department.html')
def contact(request):
    if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          subject=request.POST.get('subject')
          message=request.POST.get('message')
     
          if request.POST:
               details=Contact.objects.create(name=name,email=email,phone=phone,subject=subject,message=message)
               details.save()
               return redirect('contact')

    return render(request,'contact.html')
def branch(request):
    context={}
    o=Branch.objects.all()
    context['o']=o
    return render(request,'branch.html',context)
def appointment(request):
    if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          message=request.POST.get('message')
          age=request.POST.get('age')
          gender=request.POST.get('gender')
          address=request.POST.get('address')
          date=request.POST.get('date')
          time=request.POST.get('time')


          if request.POST:
               details=Appointment.objects.create(name=name,email=email,phone=phone,message=message,age=age,gender=gender,address=address,date=date,time=time)
               details.save()
               return redirect('appointment')
          



    return render(request,'appointment.html')
def blog(request):
    context={}
          
    m=Blog.objects.all()
    context['m']=m

    return render(request,'blog.html',context)
def subblog(request,id):

    context={}
    su=Sub_blog.objects.filter(blog=id)  
    context['su']=su

    return render(request,'subblog.html',context)

def subpackage(request,id):
    context={}
    
    # obj=Subpackage.objects.filter(package=ob)

    obj=Packages.objects.all()  
    # print("id is",id)
    su=Subpackage.objects.filter(package=id)
    # print(su)
    context['obj']=obj
    context['su']=su


    
    return render(request,'subpackage.html',context)