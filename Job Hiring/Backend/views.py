from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def job(request):
    if request.method=='POST':
        data=request.POST
        Companyn=data.get('Companyn')
        Jobtitle=data.get('Jobtitle')
        Jobdescription=data.get('Jobdescription')
        Joblocation=data.get('Joblocation')
        print(Companyn,Jobtitle,Jobdescription,Joblocation)
        
        Job.objects.create(
            Companyn=Companyn,
            Jobtitle=Jobtitle,
            Jobdescription=Jobdescription,
            Joblocation=Joblocation,
        )

        return redirect('/job')
    
    queryset=Job.objects.all()
    context={'jobs':queryset}
    return render(request,'job.html',context)

def update_job(request,id):
    queryset=Job.objects.get(id=id)

    if request.method=='POST':
        data=request.POST
        Companyn=data.get('Companyn')
        Jobtitle=data.get('Jobtitle')
        Jobdescription=data.get('Jobdescription')
        Joblocation=data.get('Joblocation')

        queryset.Companyn=Companyn
        queryset.Jobtitle=Jobtitle
        queryset.Jobdescription=Jobdescription
        queryset.Joblocation=Joblocation
        queryset.save()
        return redirect('/job')

    context={'jobs':queryset}
    return render(request,'updatejob.html',context)


def delete_job(request,id):
    queryset=Job.objects.get(id=id)
    queryset.delete()
    return redirect('/job')