from django.contrib import admin
from .models import Department,Roles
# Register your models here.

class adminDepartmentmodel(admin.ModelAdmin):
    list_display = ['department_name','department_description']
admin.site.register(Department,adminDepartmentmodel)


class adminRolesmodel(admin.ModelAdmin):
    list_display = ['role_name','role_description']
admin.site.register(Roles,adminRolesmodel)
