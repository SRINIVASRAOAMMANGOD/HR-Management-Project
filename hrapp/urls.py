from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('upload/', views.upload_file, name='upload_csv'),
    path('logout/', views.logout_view, name='logout'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/edit/<int:id>/', views.edit_employee, name='edit_employee'),
    path('employees/delete/<int:id>/', views.delete_employee, name='delete_employee'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
     path('export/employees/csv/', views.export_employees_csv, name='export_employees_csv'),
    path('export/employees/excel/', views.export_employees_excel, name='export_employees_excel'),
] 
