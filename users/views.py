from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created you are now able to login!')
            return redirect('login')
        else:
            messages.error(request, f'Account was not created try again')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
