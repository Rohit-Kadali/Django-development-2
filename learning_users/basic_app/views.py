from django.shortcuts import render
from basic_app.forms import Userinfoform, Userform
# Create your views here.

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'basic_app/index.html')



@login_required
def special(request):
    return HttpResponse(" You are Logged in, Nice!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    

def register(request):
    
    registered = False
    
    if request.method == "POST" :
        User_form = Userform(data=request.POST)
        Profile_form = Userinfoform(data=request.POST)
        
        if User_form.is_valid() and Profile_form.is_valid ():
            
            user = User_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = Profile_form.save(commit= False)
            profile.user= user
            
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                
            profile.save()
            
            registered = True
        else:
            print(User_form.errors,Profile_form.errors)  
            
    else:
        User_form = Userform()       
        Profile_form = Userinfoform()
        
    return render (request, 'basic_app/registration.html',
                                    {'user_form': User_form,
                                     'profile_form': Profile_form,
                                    'registered': registered})
    
def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user: 
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse ("Account Not Active ")
            
        else:
            print(" Someone Tried to login and Failed ")
            print("Username:{} and password{}".format(username,password))
            return HttpResponse(" Invalid Login Details Supplied ")
    else:
        return render(request, 'basic_app/login.html', {})
    
            
            
            
    