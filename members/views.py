from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth.models import Group

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            mentor_or_mentee = form.cleaned_data.get('mentor_or_mentee')
            
            # Add user to the selected group
            if mentor_or_mentee == 'mentor':
                group_obj = Group.objects.get(name='Mentors')
            elif mentor_or_mentee == 'mentee':
                group_obj = Group.objects.get(name='Mentees')
            
            user.groups.add(group_obj)

            username = form.cleaned_data.get('username')
            login(request,user)
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
        else:
            messages.error(request, 'There was an error with the registration form.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

def schedule(request):
    return render(request, 'schedule.html')

def index(request):
    return render(request, 'index.html')
