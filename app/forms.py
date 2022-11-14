from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 100)
	last_name = forms.CharField(max_length = 100)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length= 100,required= True)

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



