from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Group
from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def create_group(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        
        group = Group.objects.create(
            name=name,
            description=description,
            owner=request.user
        )
        return redirect('group_statistics', group_id=group.id)

    return render(request, 'create_group.html')

@login_required
def group_statistics(request, group_id):
    group = Group.objects.get(id=group_id)
    return render(request, 'group_statistics.html', {'group': group})

@login_required
def leaderboard(request, group_id):
    group = Group.objects.get(id=group_id)
    # Placeholder for leaderboard logic
    return render(request, 'leaderboard.html', {'group': group})