from django import forms
from django.contrib.auth.models import User
from . import models

# forms.py
from django.core.exceptions import ValidationError



#for admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


#for counsellor related form
class CounsellorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.islower() for char in password):
            raise ValidationError("Password must contain at least one lowercase letter.")
        if not any(char.isupper() for char in password):
            raise ValidationError("Password must contain at least one uppercase letter.")
        return password     
        
            
class CounsellorForm(forms.ModelForm):
    class Meta:
        model=models.Counsellor
        fields=['address','mobile','department','status','profile_pic']



#for student related form
class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.islower() for char in password):
            raise ValidationError("Password must contain at least one lowercase letter.")
        if not any(char.isupper() for char in password):
            raise ValidationError("Password must contain at least one uppercase letter.")
        return password
class StudentForm(forms.ModelForm):
    #this is the extrafield for linking Student and their assigend Counsellor
    #this will show dropdown __str__ method Counsellor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Counsellor model and return it
    assignedCounsellorId=forms.ModelChoiceField(queryset=models.Counsellor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Student
        fields=['address','mobile','status','studyArea','profile_pic']



class AppointmentForm(forms.ModelForm):
    counsellorId=forms.ModelChoiceField(queryset=models.Counsellor.objects.all().filter(status=True),empty_label="Counsellor Name and Department", to_field_name="user_id")
    studentId=forms.ModelChoiceField(queryset=models.Student.objects.all().filter(status=True),empty_label="Student Name and StudyArea", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status']


class StudentAppointmentForm(forms.ModelForm):
    counsellorId=forms.ModelChoiceField(queryset=models.Counsellor.objects.all().filter(status=True),empty_label="Counsellor Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status']


#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))




