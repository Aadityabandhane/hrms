from django.shortcuts import render,redirect,get_object_or_404
from .forms import Departmentform,userauthenticationForm,registrationform,Rolesform,EmployeeForm
from .models import Department,Roles,Employe_User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

# Email...**********

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.template.loader import render_to_string

import uuid
from django.conf import settings


from django.contrib.auth.decorators import login_required


# Create your views here.
def add(request):
    departments = Department.objects.filter(status=True)

    if request.method == 'POST':
        fm = Departmentform(request.POST)
        if fm.is_valid():
            dn=fm.cleaned_data['department_name']
            dd=fm.cleaned_data['department_description']
            reg = Department(department_name=dn,department_description=dd)
            reg.save()
            fm = Departmentform()  
    else:
        departments = Department.objects.filter(status=True)
        fm = Departmentform()   
        
    return render(request, 'add.html',{'form':fm, 'deprt':departments})

def home(request):
    return render(request,'home.html')
    



import datetime
def logindetails(request):
    if request.method=="POST":
        uname=request.POST["username"]
        upass=request.POST["password"]
        user=authenticate(request,username=uname,password=upass)
        
        if user is not None:
            login(request,user)
            response=redirect('home')
            request.session['username']=uname
            response.set_cookie('username',uname)
            response.set_cookie('time',datetime.datetime.now())
            return response
        else:
            LDF=userauthenticationForm()
            return render(request,"login.html",{"LDF":LDF,'msg':'Worong password or username...!'})
    else:
        LDF=userauthenticationForm()
        return render(request,"login.html",{"LDF":LDF})
    
def logout_details(request):
    logout(request)
    return redirect('home')

def delete_product(request, id):
    deletedept = Department.objects.get(id=id)
    print('got', deletedept)
    deletedept.status = False
    deletedept.save()
    print() 
    fm = Departmentform()   
    return redirect('add')
 

def updateprod(request, id):
    # Safely get the department object or return a 404 if not found
    product = get_object_or_404(Department, id=id)
    
    if request.method == "POST":
        form = Departmentform(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('add')
        else:
            # Return the form with errors to the template
            return render(request, "update.html", {"form": form})
    else:
        # Initialize the form with the existing product instance
        form = Departmentform(instance=product)
        return render(request, "update.html", {"form": form})


def register(request):
    if request.method=="POST":
        RF=registrationform(request.POST)
        if RF.is_valid():
            RF.save()
            return redirect('home')
        else:
            RF=registrationform()
            return render(request,"register.html",{"RF":RF,'msg':'Worong credentials...!'})
    else:
        RF=registrationform()
        return render(request,"register.html",{"RF":RF})


def roles(request):
    role = Roles.objects.filter(status=True)

    if request.method == 'POST':
        fm = Rolesform(request.POST)
        if fm.is_valid():
            dn=fm.cleaned_data['role_name']
            dd=fm.cleaned_data['role_description']
            reg = Roles(role_name=dn,role_description=dd)
            reg.save()
            fm = Rolesform()  
    else:
        role = Roles.objects.filter(status=True)
        fm = Rolesform()   
        
    return render(request, 'roles.html',{'form':fm, 'role':role})


def deleterole(request, id):
    deleterole = Roles.objects.get(id=id)
    print('got', deleterole)
    deleterole.status = False
    deleterole.save()
    print() 
    fm = Rolesform()   
    return redirect('roles')

 

def updaterole(request, id):
    # Safely get the department object or return a 404 if not found
    role = get_object_or_404(Roles, id=id)
    
    if request.method == "POST":
        form = Rolesform(request.POST, request.FILES, instance=role)
        if form.is_valid():
            form.save()
            return redirect('roles')
        else:
            # Return the form with errors to the template
            return render(request, "updaterole.html", {"form": form})
    else:
        # Initialize the form with the existing product instance
        form = Rolesform(instance=role)
        return render(request, "updaterole.html", {"form": form})


from django.contrib import messages


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmployeeForm
from .models import Employe_User, Department, Roles

def create_employee(request):
    departments = Department.objects.filter(status=True)
    roles = Roles.objects.filter(status=True)
    employees = Employe_User.objects.all()  # ✅ Fetch all employees

    if request.method == "POST":
        print("🚀 Form Data Received:", request.POST)  # Debugging

        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)

            # Validate department
            department_id = request.POST.get('dept')
            department = Department.objects.filter(id=department_id, status=True).first()
            if not department:
                messages.error(request, "Invalid or inactive department selected")
                return render(request, 'employee_list.html', {
                    'form': form, 'departments': departments, 'roles': roles, 'employees': employees
                })

            # Validate role
            role_id = request.POST.get('role')
            role = Roles.objects.filter(id=role_id, status=True).first()
            if not role:
                messages.error(request, "Invalid or inactive role selected")
                return render(request, 'employee_list.html', {
                    'form': form, 'departments': departments, 'roles': roles, 'employees': employees
                })

            # Assign department and role
            employee.department = department
            employee.role = role
            employee.save()

            messages.success(request, "Employee created successfully!")
            return redirect('employee_list')

        else:
            messages.error(request, "Form is invalid. Please check the inputs.")
            print(" Form Errors:", form.errors)  # Debugging

    else:
        form = EmployeeForm()

    return render(request, 'employee_list.html', {
        'form': form, 'departments': departments, 'roles': roles, 'employees': employees
    })


def deleteemployee(request, emp_id):
    employee = get_object_or_404(Employe_User, employee_id=emp_id)  # ✅ Correct lookup
    print("Employee found:", employee)
    employee.delete()
    print("Employee deleted successfully")
    messages.success(request, "Employee deleted successfully!")
    return redirect('employee_list')  # ✅ Ensure 'employee_list' is a valid URL name




def updateemployee(request, emp_id):
    Employe = get_object_or_404(Employe_User, employee_id=emp_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES,instance=Employe)
        if form.is_valid():
            form.save()
            return redirect('updateemployee',emp_id=emp_id)
        else:
            # Return the form with errors to the template
            return render(request, "updateemployee.html", {"form": form})
    else:
        # Initialize the form with the existing product instance
        form = EmployeeForm(instance=Employe)
        return render(request, "updateemployee.html", {"form": form})



def forgot_password(request):          

    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email).first()
        if user:
            token = default_token_generator.make_token(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = request.build_absolute_uri(f'/reset_password/{uidb64}/{token}/')           
            send_mail(
                'Password Reset',
                f'Click the given link to reset your password: {reset_url}',
                settings.EMAIL_HOST_USER,  # Use a verified email address
                [email],
                fail_silently=False,
            )
            return redirect('passwordresetdone')
        else:
            print('I am executed')
           
    print('I am executed')
    return render(request,'forgot_password.html')


def reset_password(request, uidb64, token):
    if request.method == 'POST':
        password = request.POST['password']
        print(password)
        password2 = request.POST['password2']
        print(password2)
        if password == password2:
            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
                if default_token_generator.check_token(user, token):
                    user.set_password(password)
                    user.save()
                    return redirect('login')
                else:
                    return HttpResponse('Token is invalid', status=400)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                return HttpResponse('Invalid link', status=400)
        else:
            return HttpResponse('Passwords do not match', status=400)
    return render(request, 'reset_password.html')

def password_reset_done(request):
    return render(request, 'password_reset_done.html')

