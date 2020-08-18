from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib import messages
from users.models import Profile
from users.forms import UpdateProfileForm

def login_view(request):
    """Allows the user to login to our app"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        account = authenticate(request, username=username, password=password)

        if account:
            login(request, account)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', { 'error': 'Invalid username or password' })

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    """Handles user logout from their account"""
    logout(request)
    return redirect('login')

def signup_view(request):
    """Handles user sign up"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request, 'users/signup.html', { 'error': 'Passwords doesn\'t match' })

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', { 'error': 'Username is already in use' })

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        messages.success(request, 'You\'ve registered successfully')

        return redirect('login')

    return render(request, 'users/signup.html')

@login_required
def update_profile(request):
    """Let the user update its profile"""
    profile = request.user.profile

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            profile.profile_picture = data['profile_picture']
            profile.web_site = data['web_site']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.save()

            messages.success(request, 'Your profile has been updated!')

            return redirect('update_profile')
    else:
        form = UpdateProfileForm()

    return render(
        request,
        'users/update_profile.html',
        {
            'profile': profile,
            'user': request.user,
            'form': form,
        }
    )