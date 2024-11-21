from django import forms
from basic_app.models import UserInfo
from django.contrib.auth.models import User

class Userform(forms.ModelForm) :
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta() :
        model = User
        fields = ('username','email','password')
        
class Userinfoform(forms.ModelForm) :
    class Meta() :
        model = UserInfo
        fields = ('portfolio_site', 'profile_pic')
        