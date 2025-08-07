from django.shortcuts import render, redirect
from .forms import StudentRegisterForm,StudentForm
# from .models import Student
# from django.contrib import messages

# Create your views here.
def home(request):
    stats=[
        {
            'title': 'Total Students',
            'value': 1280,
            'text_color': 'text-primary'
        },
        {
            'title': 'Total Payments',
            'value': 'Rs. 750000',
            'text_color': 'text-green-600'
        },
        {
            'title': 'Pending Payments',
            'value': 'Rs. 120000',
            'text_color': 'text-red-600'
        },
        {
            'title': 'Active Classes',
            'value': 12,
            'text_color': 'text-secondary'
        },
        {
            'title': 'Total Students Overall just making it long to see how it works, even making it the longerst as much as possilbe  ksfnsk ns sf essjjvs js jgs js dj',
            'value': 45000,
            'text_color': 'text-secondary'
        },
        {
            'title': 'Total Payments Overall',
            'value': 'Rs. 7,50,000',
            'text_color': 'text-green-600'
        },
    ]
   
    context = {
        'stats': stats
    }
    return render(request, 'app/dashboard.html', context)  # Add context here

def student(request):
    # Create a separate context for student view if needed
    return render(request, 'app/student.html')

# def student_register(request):
#     if request.method == 'POST':
        
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
        
#         print("Name:",first_name, last_name)
#         print("Email:",email)
#         print("Phone:",phone)
        
#         errors={}
#         if not len(phone) == 10:
#             errors['phone'] = "Phone number should be 10 digits"
        
#         if len(errors.keys()) > 0:
#             from_data={
#                 'first_name': first_name,
#                 'last_name': last_name,
#                 'email': email,
#                 'phone': phone
#             }
#             context={
#                 "errors": errors,
#                 "from_data": from_data
#             }
#             return render(request, 'app/student_register.html', context)
        
#         return redirect('home')
    
#     return render(request, 'app/student_register.html')


def student_register(request):
    if request.method == 'POST':
        print("post data", request.POST)
        form = StudentForm(request.POST)
        
        if not form.is_valid():
            print("-----    Invalid form    -----", form.errors)
            context={
                'form': form
            }
            return render(request, 'app/student_register.html', context)
        
        print("-----    Valid form    -----")
        form.save()
        
        return redirect('student_register')
    
    form =StudentForm()
    
    context={
        'form': form
    }
    
    return render(request, 'app/student_register.html', context )