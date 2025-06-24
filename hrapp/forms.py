from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
# the below SignupForm is actully not used 
# class SignupForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']


# to use 
# update views.py forms.TypedChoiceField(from .forms import SignupForm

# def signup_view(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)  # don't save password yet
#             user.set_password(form.cleaned_data['password'])  # hash password
#             user.save()
#             return redirect('login')
#     else:
#         form = SignupForm()

#     return render(request, 'hrapp/signup.html', {'form': form})
# , required=False)

# signip.html to
# <form method="POST">
#     {% csrf_token %}
#     {{ form.as_p }}  <!-- This will auto-display username, email, and password fields -->
#     <button type="submit">Sign Up</button>
# </form>






class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'company_name','profile_image']
