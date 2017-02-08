from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from .models import *


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', locals())


def register(request):
    if request.POST:
        first_name = request.POST.get('first-name', '')[:30]
        last_name = request.POST.get('last-name', '')[:30]
        email = request.POST.get('email', '')[:150]
        username = request.POST.get('email', '')[:150]
        country = request.POST.get('country', '')
        password = request.POST.get('password', '')

        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.is_staff = False
            user.is_superuser = False
            user.is_active = True
            user.profile.country = country
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')

        except IntegrityError:
            error = True

    return render(request, 'register.html', locals())


@login_required
def account_edit(request):
    user = request.user

    if request.POST:
        first_name = request.POST.get('first-name', '')[:30]
        last_name = request.POST.get('last-name', '')[:30]
        country = request.POST.get('country', '')
        password = request.POST.get('password', '')

        user.first_name = first_name
        user.last_name = last_name
        user.profile.country = country

        if user.check_password(password):
            user.save()
            form_message = 'Profile changed successfully.'
        else:
            form_message = 'Invalid password.'

    return render(request, 'edit-account.html', locals())


@login_required
def change_password(request):
    if request.POST:
        user = request.user
        current_password = request.POST.get('current-password', '')
        new_password = request.POST.get('new-password', '')

        if user.check_password(current_password):
            user.set_password(new_password)
            user.save()
            form_message = 'Password changed successfully.'
        else:
            form_message = 'Invalid current password.'

    return render(request, 'change-password.html', locals())
