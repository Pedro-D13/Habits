#  non-restful imports
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from users.models import Profile


# Restful view imports
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from users.serializers import UserSerializer, GroupSerializer

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
    user_profile = Profile.objects.filter(user=request.user)
    return render(request, 'users/profile.html', {'user_person': user_profile})

#  Viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
