from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')

    form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/reg_form.html', context)


def profile(request):
    context = {
        'user': request.user,
    }
    return render(request, 'accounts/profile.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts:user_profile')

    form = EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'accounts/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:user_profile')
        else:
            return redirect('accounts:change_password')

    form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'accounts/change_password.html', context)
