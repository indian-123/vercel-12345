from django.shortcuts import redirect, render
from .models import Datas
from django.contrib import messages
import os


# Create your views here.
def home(request):
    # return render(request,'home.html')
    return render(request,'home.html')
    
    
    
    
def table(request):
    mydata=Datas.objects.all()
    if(mydata!=''):
        return render(request,'index.html',{'datas':mydata})
    else:
        return render(request,'index.html')
    

def adddata(request):
   
    if request.method=="POST":
          
        pame=request.POST['nam']
        pge=request.POST['passwords']
        pddress=request.POST['address']
        pontact=request.POST['contact']
        pail=request.POST['mail']
        pimage=request.FILES.get('img1','imges/IMG_20201029_120332.jpg')
        

        

        if Datas.objects.filter(Mail=pail).exists():
            messages.warning(request,'email already register')
            return redirect('index')
        elif  Datas.objects.filter(Contact=pontact).exists():
           
            messages.warning(request,'contact already register')
            return redirect('index')
        else:
            messages.success(request,'THE DATA ADDED SUCCESSFULLY')
            obj=Datas()
            obj.Name=pame
            obj.Password=pge
            obj.Address=pddress
            obj.Contact=pontact
            obj.Mail=pail
            obj.image=pimage
            obj.save()
            return redirect('index')

def update(request,id):
    mydata=Datas.objects.get(id=id)
    
    if request.method=='POST':
       
        if len(request.FILES)!=0:
            if len(mydata.image)>0:
                os.remove(mydata.image.path)
            mydata.image=request.FILES['img1']
        # filename=request.FILES['img1'].
        pame=request.POST['nam']
        pge=request.POST['passwords']
        pddress=request.POST['address']
        pontact=request.POST['contact']
        pail=request.POST['mail']
        mydata.Name=pame
        mydata.Password=pge
        mydata.Address=pddress
        mydata.Montact=pontact
        mydata.Mail=pail
        mydata.save()
        messages.success(request,'UP TO DATE SUCESSFULLY') #tags means success or info or danger or primary etc....
        return redirect('index')
    context={'data':mydata}
    return render(request,'update.html',context)

  
def delete(request,id):
          

        mydata=Datas.objects.get(id=id)
        mydata.delete()
        messages.warning(request,'DATA DELETED SUCCESSFULLY') 
        return redirect('index')

def login(request):
    return render(request,'login.html')



def logcon(request):
     if request.method == 'POST':
        pail=request.POST['mail']
        pge = request.POST['passwords']
        if Datas.objects.filter(Mail=pail).exists():
            
            if Datas.objects.filter(Password=pge).exists():
                b= Datas.objects.get(Mail=pail)
                return render(request,'home.html',{'pics':b})
            else:
                messages.warning(request,'LOGIN FAILED')
                return redirect('login')
            
            
             
        else:
            messages.warning(request,'LOGIN FAILED')
            return redirect('login')
    
