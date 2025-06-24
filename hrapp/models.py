from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Employee(models.Model):
    hr_user = models.ForeignKey(User, on_delete=models.CASCADE)  # 👈 New field linking to logged-in HR,hr_user → tells us this is a foreign key to the HR user.
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.department})"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    #profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # 👈 Add this line
    profile_image = CloudinaryField('image', blank=True, null=True) #cloudinary
    def __str__(self):
        return self.user.username
class HRDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100, blank=True, null=True)  # Optional field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
