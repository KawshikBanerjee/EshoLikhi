from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm 


def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully Created Account for {username}! You Are Now Able to Log In')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form': form})


@login_required

def profile(request):
    return render(request, 'user/profile.html')