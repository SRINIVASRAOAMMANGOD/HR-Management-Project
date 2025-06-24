from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User
from .models import Employee, UserProfile, HRDetails
import pandas as pd
import csv
from django.http import HttpResponse

@login_required
def export_employees_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Phone', 'Department', 'Role', 'Salary'])

    employees = Employee.objects.filter(hr_user=request.user)
    for emp in employees:
        writer.writerow([emp.name, emp.email, emp.phone, emp.department, emp.role, emp.salary])

    return response


@login_required
def export_employees_excel(request):
    employees = Employee.objects.filter(hr_user=request.user)
    data = [
        {
            'Name': emp.name,
            'Email': emp.email,
            'Phone': emp.phone,
            'Department': emp.department,
            'Role': emp.role,
            'Salary': emp.salary,
        }
        for emp in employees
    ]

    df = pd.DataFrame(data)
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="employees.xlsx"'
    df.to_excel(response, index=False)

    return response



@never_cache
@login_required
def profile_view(request):
    user = request.user
    try:
        hr = HRDetails.objects.get(user=user)
    except HRDetails.DoesNotExist:
        return redirect('logout')
    profile, _ = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        hr.phone = request.POST.get('phone')
        hr.company = request.POST.get('company')
        if 'profile_image' in request.FILES:
            profile.profile_image = request.FILES['profile_image']
           

        user.save()
        hr.save()
        profile.save()  # ✅ Save image update
    return render(request, 'hrapp/profile.html', {
        'user': user,
        'hr': hr,
        'profile' : profile,
    })


@never_cache
@login_required
def dashboard_view(request):
    return render(request, 'hrapp/dashboard.html')


@never_cache
@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('employee_file'):
        file = request.FILES['employee_file']
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)

        for _, row in df.iterrows():
            Employee.objects.create(
                hr_user=request.user,
                name=row['Name'],
                email=row['Email'],
                phone=row['Phone'],
                department=row['Department'],
                role=row['Role'],
                salary=row['Salary']
            )
        return redirect('dashboard')
    return render(request, 'hrapp/csvfile.html')


@never_cache
@login_required
def employee_list(request):
    employees = Employee.objects.filter(hr_user=request.user)
    return render(request, 'hrapp/employee_list.html', {'employees': employees})


@never_cache
@login_required
def add_employee(request):
    if request.method == 'POST':
        Employee.objects.create(
            hr_user=request.user,
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            department=request.POST['department'],
            role=request.POST['role'],
            salary=request.POST['salary']
        )
        return redirect('employee_list')
    return render(request, 'hrapp/add_employee.html')


@never_cache
@login_required
def edit_employee(request, id):
    employee = Employee.objects.get(id=id, hr_user=request.user)
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.phone = request.POST['phone']
        employee.department = request.POST['department']
        employee.role = request.POST['role']
        employee.salary = request.POST['salary']
        employee.save()
        return redirect('employee_list')
    return render(request, 'hrapp/edit_employee.html', {'employee': employee})


@never_cache
@login_required
def delete_employee(request, id):
    employee = Employee.objects.get(id=id, hr_user=request.user)
    employee.delete()
    return redirect('employee_list')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if HRDetails.objects.filter(user=user).exists():
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'hrapp/index.html', {'error': 'HR Profile missing. Contact Admin.'})
        else:
            return render(request, 'hrapp/index.html', {'error': 'Invalid credentials'})

    return render(request, 'hrapp/index.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'hrapp/signup.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, email=email, password=password)
        HRDetails.objects.create(user=user, phone=phone)
        return redirect('login')

    return render(request, 'hrapp/signup.html')


def logout_view(request):
    logout(request)
    return redirect('login')