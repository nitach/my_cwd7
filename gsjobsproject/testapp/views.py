from django.shortcuts import render
from testapp.models import HydJobs,BangaloreJobs,PuneJobs
# Create your views here.

def homepage_view(request):
    return render(request,'testapp/index.html')

def hydjobs_view(request):
    jobs_list = HydJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)
def bangluru_view(request):
    jobs_list = BangaloreJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/Bangalore.html',context=my_dict)
