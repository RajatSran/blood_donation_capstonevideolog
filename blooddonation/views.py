from django.shortcuts import render
from . import models

def home(request):
    return render(request,'form.html')
def fpage(request):
    return render(request,'blooddonation.html')

def ins_upd_del(request):
    if request.method == 'POST':
        if request.POST["action"]=="Insert":
            obj=models.blooddonation()
        elif request.POST["action"]=="Update":
            nameid=request.POST["name"]
            obj=models.blooddonation.objects.get(name=nameid)
        elif request.POST["action"]=="Delete":
            nameid=request.POST["name"]
            obj=models.blooddonation.objects.get(name=nameid)
            obj.delete()
            return render(request,'form.html')
        obj.name=request.POST["name"]
        obj.age=request.POST["age"]
        obj.weight=request.POST["weight"]
        # obj.des=request.POST["discp"]
        obj.bloodgroup=request.POST["bloodgroup"]
        try:
                obj.chk1=request.POST["chk1"]
        except:
                obj.chk1=False
        try:
                obj.chk2=request.POST["chk2"]
        except:
                obj.chk2=False
        try:
                obj.chk3=request.POST["chk3"]
        except:
                obj.chk3=False
        try:
                obj.chk4=request.POST["chk4"]
        except:
                obj.chk4=False
        obj.dat=request.POST["date"]
        obj.radio=request.POST["rd"]
        obj.img=request.FILES["img"]
        obj.save()
    return render(request,'form.html')

def disp(request):
    obj=models.blooddonation.objects.all()
    return render(request,'blooddonation.html',{"all_obj":obj})

    