from django.shortcuts import redirect, render
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm , JobForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter


def job_list(request):
    job_list = Job.objects.all()  # its queryset    see   queryset  in the Documentation

    ## filters
    myfilter = JobFilter(request.GET,queryset=job_list)
    job_list = myfilter.qs


    paginator = Paginator(job_list, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number)


#    of any Context
#? {{context_name in Template_file} : name in view_function}            
    context = {'jobs' :page_obj , 'myfilter' : myfilter} # its name in template file

 #                           html file template   
    return render(request,'job/job_list.html',context)       # then go adjast the template_html file job_list.html   add the Context


#                      , int
def job_detail(request , slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method=='POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            print('DOne')

    else:
        form = ApplyForm()


    context = {'job' : job_detail , 'form1':form}
    return render(request,'job/job_detail.html',context)


@login_required
def add_job(request):
    if request.method=='POST':
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form = JobForm()

    return render(request,'job/add_job.html',{'form':form})