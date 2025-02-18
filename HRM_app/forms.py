from django import forms
from .models import Department,Roles,Employe_User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



class Departmentform(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name','department_description']
        widgets = {
            'department_name' : forms.TextInput(attrs={'class':'form-control'}),
            'department_description' : forms.TextInput(attrs={'class':'form-control'}),
        }

class userauthenticationForm (AuthenticationForm):
    username=forms.CharField(label="Enter username",widget=forms.TextInput(attrs={'class':'form-control'})),
    password=forms.CharField(label="Enter password",widget=forms.PasswordInput(attrs={'class':'form-control'})),   
    
    class Meta:
        model=User
        fields=['username','password']

class registrationform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
        
        labels={
            'username':'Enter Username',
            'first_name':'Enter first name',
            'last_name':'Enter Last name',
            'email':'Enter Email',
            'password1':'Enter password',
            'password2':'Enter confirm password',
        }
        
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
        }
 

class loginform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password']
        
        labels={
            'username':'Enter Username',
            'password':'Enter password',
        }
        
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }


class Rolesform(forms.ModelForm):
    class Meta:
        model = Roles
        fields = ['role_name','role_description']
        widgets = {
            'role_name' : forms.TextInput(attrs={'class':'form-control'}),
            'role_description' : forms.TextInput(attrs={'class':'form-control'}),
        }



class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employe_User
        fields = [
            'first_name','last_name','email','mobile','role','dept','reporting_manager', 
            'date_of_joining','username', 'password'
        ]
        
        widgets = {
            'password': forms.PasswordInput(),
            'date_of_joining': forms.DateInput(attrs={'type': 'date'}),
        }

    first_name = forms.CharField(max_length=100, required=True, label="First Name")
    last_name = forms.CharField(max_length=100, required=True, label="Last Name")
    email = forms.EmailField(max_length=100, required=True, label="Email")
    mobile = forms.CharField(max_length=100, required=True, label="Mobile Number")
    role = forms.ModelChoiceField(queryset=Roles.objects.all(), required=True, label="Select Role")
    dept = forms.ModelChoiceField(queryset=Department.objects.all(), required=True, label="Select Department")
    reporting_manager = forms.ModelChoiceField(
        queryset=Employe_User.objects.all(), required=False, label="Allocate Reporting Manager"
    )
    date_of_joining = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Date of Joining")
    username = forms.CharField(max_length=100, required=True, label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label="Set Password")
