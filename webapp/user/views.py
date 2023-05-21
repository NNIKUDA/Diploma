from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash

from .forms import SingInForm, SingUpForm, ProfileForm, MyPasswordResetForm, MySetPasswordForm, \
    MyPasswordChangeForm


def index(request):
    return render(request, 'index.html')


def login_view(request):
    context = {
        'sing_up_form': SingUpForm(),
        'sing_in_form': SingInForm(),
        'active': 'login',
    }
    return render(request, 'login.html', context=context)


@require_http_methods(['POST'])
def sing_in(request):
    sing_in_form = SingInForm(request.POST)
    if sing_in_form.is_valid():
        remember_me = sing_in_form.cleaned_data['remember_me']
        user = authenticate(email=sing_in_form.cleaned_data["email"], password=sing_in_form.cleaned_data["password"])
        if user:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)
            return redirect(reverse('home'))
        else:
            sing_in_form.add_error(None, "Invalid email or password")
    context = {
        'sing_up_form': SingUpForm(),
        'sing_in_form': sing_in_form,
        'active': 'login',
    }
    return render(request, 'login.html', context=context)


@require_http_methods(['POST'])
def sing_up(request):
    sing_up_form = SingUpForm(request.POST)
    if sing_up_form.is_valid():
        if sing_up_form.cleaned_data['register_policy']:
            user = sing_up_form.save()
            if user:
                login(request, user)
            else:
                print(user)
            return redirect(reverse('home'))

    context = {
        'sing_up_form': sing_up_form,
        'sing_in_form': SingInForm(),
        'active': 'register',
    }
    return render(request, 'login.html', context=context)


def dashboard(request):
    user = request.user
    context = {
        'active': 'dashboard',
        'change_password_form': MyPasswordChangeForm(user)
    }
    if request.method == 'GET':
        initial_data = {
            'username': user.username if user.username else '',
            'new_email': user.email,
            'first_name': user.first_name if user.first_name else '',
            'last_name': user.last_name if user.last_name else '',
            'email': user.email
        }
        profile_form = ProfileForm(initial_data)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            user = profile_form.save()
        context['active'] = 'account'

    context['profile_form'] = profile_form

    return render(request, 'dashboard.html', context=context)


def change_password(request):
    user = request.user
    change_password_form = MyPasswordChangeForm(user, request.POST)
    initial_data = {
        'username': user.username if user.username else '',
        'new_email': user.email,
        'first_name': user.first_name if user.first_name else '',
        'last_name': user.last_name if user.last_name else '',
        'email': user.email
    }
    context = {
        'active': 'change_password',
        'profile_form': ProfileForm(initial_data),
        'change_password_form': change_password_form,
    }
    if request.method == 'POST':
        if change_password_form.is_valid():
            user = change_password_form.save()
            update_session_auth_hash(request, user)
            change_password_form.add_error(None, 'Password changed')
    return render(request, 'dashboard.html', context=context)


# @require_http_methods(['POST'])
def sing_out(request):
    logout(request)
    return redirect(reverse('login'))


class MyPasswordResetView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    form_class = MyPasswordResetForm
    success_url = reverse_lazy("home")
    success_message = 'Mail was send'


class MyPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    form_class = MySetPasswordForm
    success_url = reverse_lazy("login")
    success_message = 'Password changed'



