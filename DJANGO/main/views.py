from django.shortcuts import render,redirect
from .models import Task,School
# from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from django.http import HttpResponse

class SchoolDelete(DeleteView):
    model=School
    # fields="__all__"
    success_url=reverse_lazy('schools_list')
    
class SchoolUpdate(UpdateView):
    model=School
    fields="__all__"
    success_url=reverse_lazy('schools_list')


class SchoolCreate(CreateView):
    model=School
    fields="__all__"
    success_url=reverse_lazy('schools_list')
    
class SchoolDetail(DetailView):
    model = School
    # context_object_name = 'school'
    # template_name = 'main/school_detail.html'
    
class SchoolView(ListView):
    model = School
    
    
    
# def school_detail(request,school_id):
#     print("School's Detail Page",school_id)
    
    
# def schools(request):
#     print("School's page")
    
    



# tasks=[
        
#             {'title': "This is task 1",'desc':"This is task 1 description"},
#             {'title': "This is task 2",'desc':"This is task 2 description"},
#             {'title': "This is task 2",'desc':"This is task 2 description"},
#             {'title': "This is task 2",'desc':"This is task 2 description"},
#     ]


# Create your views here.
def home(request):
    # print("HOME PAGE ")
    # user_name="Sushant"
    # global tasks
    
    tasks=Task.objects.all()
    context = {'tasks':tasks}
    return render(request, "main/home.html",context)

def create_task(request):
    
    if request.method=="POST":
        print("--------THIS IS POST request----------")
        data=request.POST
        task_title=data.get("title")
        task_desc=data.get("desc")
        
        Task.objects.create(title=task_title,desc=task_desc)
        
        return redirect(home)
        
        # new_task={
        #     "title":task_title,
        #     "desc":task_desc
        # }
        # global tasks
        # tasks.append(new_task)
        
        # # print(data)
        
    return render(request, "main/create_task.html")

