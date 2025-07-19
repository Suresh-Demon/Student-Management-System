from django.shortcuts import render,redirect
from .models import student
from django.db.models import Q
from django.contrib import messages


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
       data=student.objects.all().order_by('id')
       return render(request, 'show.html', {'d': data})



def editstudent(request,uid):
      if request.method=='POST':
        na=request.POST['uname']
        em=request.POST['emailid']
        mo=request.POST['mobileno']
        add=request.POST['addre']
        co=request.POST['dcourse']
        data=student.objects.filter(id=uid)
        data.update(name=na,email=em,mobile=mo,address=add,course=co)

        messages.success(request, "Student updated successfully!")
        return redirect('/')
      else:
          data=student.objects.get(id=uid)
          return render(request,'update.html',{'d':data})
      

def deletestudent(request, uid):
    data = student.objects.filter(id=uid)
    data.delete()
    messages.success(request, "Student deleted successfully!")
    return redirect('/')


def search_box(request):
    query = request.GET.get('q', '').strip()  
    if query:
        studentdata = student.objects.filter(
            Q(name__icontains=query) |
            Q(address__icontains=query)
        )
    else:
        studentdata = student.objects.all()

    context = {
        
          'd': studentdata,
          'query': query
    }

    return render(request, 'show.html', context)

           