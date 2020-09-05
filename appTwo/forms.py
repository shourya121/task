from django import forms
from django.contrib.auth.models import User
from appTwo.models import UserProfileInfo





class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_Password=forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model=User
        fields=('first_name','last_name','email','username','password')
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_Password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class UserProfileInfoForm(forms.ModelForm):
    unique_id=forms.CharField(min_length=6)
    class Meta():
        model=UserProfileInfo
        fields=('profile_pic','unique_id','age')
