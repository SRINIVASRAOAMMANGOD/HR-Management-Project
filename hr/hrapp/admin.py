from django.contrib import admin
from .models import HRDetails, Employee
from import_export.admin import ExportMixin  # Requires: pip install django-import-export

# HRDetails Admin
@admin.register(HRDetails)
class HRDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'company', 'created_at')
    search_fields = ('user__username', 'phone', 'company')

# Employee Admin with Export Feature
@admin.register(Employee)
class EmployeeAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'department', 'role', 'salary', 'hr_user')
    search_fields = ('name', 'email', 'department', 'role')
    list_filter = ('department', 'role')
