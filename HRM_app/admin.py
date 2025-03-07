from django.contrib import admin
from .models import Department,Roles,Employe_User,PerformanceReview
# Register your models here.

class adminDepartmentmodel(admin.ModelAdmin):
    list_display = ['department_name','department_description']
admin.site.register(Department,adminDepartmentmodel)


class adminRolesmodel(admin.ModelAdmin):
    list_display = ['role_name','role_description']
admin.site.register(Roles,adminRolesmodel)


class adminEmployeemodel(admin.ModelAdmin):
    list_display = ['employee_id','first_name','username']
admin.site.register(Employe_User,adminEmployeemodel)


class adminreviewmodel(admin.ModelAdmin):
    list_display = ['review_title','employee','review_period','comments']
admin.site.register(PerformanceReview,adminreviewmodel)

 


from .models import Task, TaskAssignment

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'task_priority', 'start_date', 'end_date', 'task_type', 'created_at', 'updated_at')
    search_fields = ('task_title', 'task_priority', 'task_type')
    list_filter = ('task_priority', 'task_type', 'start_date', 'end_date')

@admin.register(TaskAssignment)
class TaskAssignmentAdmin(admin.ModelAdmin):
    list_display = ('task', 'employee', 'assigned_by', 'assigned_date', 'status', 'completed_at')
    search_fields = ('task_task_title', 'employeefirst_name', 'assigned_by_first_name', 'status')
    list_filter = ('status', 'assigned_date', 'completed_at')
 