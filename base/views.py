from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from pindia import pindia
from tjobs import tjobs

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def segment(request):
    segment_context = None
    if request.method == 'POST':
        position = request.POST.get('role')
        location = request.POST.get('location')
        unfam_skills = request.POST.get('exskills').strip(',')

        p_list = pindia(position,location,unfam_skills)
        t_list = tjobs(position,location,unfam_skills)

        segment_context = {
            "p_data" : p_list,
            "t_data" : t_list
        }

    return render(request,'segment.html',{"job_info":segment_context})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(username = username):
            messages.error(request,'Username already exists! Please enter a different username')
            return redirect('index')
        if User.objects.filter(email = email):
            messages.error(request,'Email already in use! Please enter a different email')
            return redirect('index')
        if password1 != password2:
            messages.error(request,'Passwords arent matching!')
            return redirect('index')

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password1)
        user.save()

        messages.success(request, 'You have been successfully registered into JOBCUT!')
        print('inside signup\n')
        return redirect('signin')

    return render(request,'signup.html')

def signin(request):
    print('exterior signin')
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')

        user = authenticate(username = username, password = password1)
        print('\ninside signin')
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('\ndidnt work')
            messages.error(request, 'Bad credentials')
            return render(request, 'signin.html')

    return render(request,'signin.html')

@login_required(login_url='/home/')
def signout(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect('signin')
