from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import job
from .form import ApplyForm , Jobform
from .filters import JobFilter
# Create your views here.



def job_list(request):
    job_list = job.objects.all()
    
    #Filter
    myfilter = JobFilter(request.GET, queryset=job_list)
    job_list = myfilter.qs
    paginator = Paginator(job_list, 3) # Show 3 jobs per page
    page_namber = request.GET.get('page')
    page_obj = paginator.get_page(page_namber)
    
    context = {'jobs': page_obj,'myfilter':myfilter}
    return render(request , 'job/job_list.html',context) 


def job_detail(request, slug):
    job_detail = job.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform =form.save(commit=False)
            myform.job = job_detail
            myform.save()
    
    else:
        form = ApplyForm()
    context = {'job': job_detail , 'form1': form}
    return render(request , 'job/job_detail.html',context)





@login_required
def add_job(request):
    
    if request.method == 'POST':
        form = Jobform(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('job:job_list'))
    else:
        form = Jobform()        
    
    
    return render(request , 'job/add_job.html', {'form' : form})
    