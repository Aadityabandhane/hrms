from django.urls import path
from .import views

urlpatterns = [
     path('add',views.add,name="add"),
     path('',views.home,name="home"),
     path('delete/<int:id>/', views.delete_product, name='deleteprod'), 
     path('updateprod/<int:id>/',views.updateprod,name='updateprod'),    
     path('register/',views.register,name="register"),
     path('login/',views.logindetails,name="login"),
     path('logout1/',views.logout_details,name="logout1"),
     path('roles/',views.roles,name="roles"),
     path('deleterole/<int:id>/', views.deleterole, name='deleterole'), 
     path('updaterole/<int:id>/',views.updaterole,name='updaterole'),
     path('employees/', views.create_employee, name='employee_list'),
     path('deleteemployee/<int:emp_id>/', views.deleteemployee, name='deleteemployee'),
     path('updateemployee/<int:emp_id>/',views.updateemployee,name='updateemployee'),
     path('forgotpassword/',views.forgot_password, name="forgotpassword"),
     path('reset_password/<uidb64>/<token>/', views.reset_password, name='resetpassword'),
     path('password_reset_done/', views.password_reset_done, name='passwordresetdone'),
    
 

]

