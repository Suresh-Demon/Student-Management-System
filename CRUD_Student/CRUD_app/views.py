from django.shortcuts import render,redirect
from .models import student

# Create your views here.

def studentdata(request):
    if request.method=='POST':
        na=request.POST['uname']
        em=request.POST['emailid']
        mo=request.POST['mobileno']
        add=request.POST['addre']
        co=request.POST['dcourse']
        data=student.objects.create(name=na,email=em,mobile=mo,address=add,course=co)
        data.save()

        return redirect('/')
    else:
        # return render(request,'home.html')
       data=student.objects.all()
       return render(request,'show.html',{'d':data})


def editstudent(request,uid):
      if request.method=='POST':
        na=request.POST['uname']
        em=request.POST['emailid']
        mo=request.POST['mobileno']
        add=request.POST['addre']
        co=request.POST['dcourse']
        data=student.objects.filter(id=uid)
        data.update(name=na,email=em,mobile=mo,address=add,course=co)
        return redirect('/')
      else:
          data=student.objects.get(id=uid)
          return render(request,'update.html',{'d':data})
      

def deletestudent(request,uid):
    data=student.objects.filter(id=uid)   
    data.delete()
    return redirect('/')   
