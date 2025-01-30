from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
import re
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def user_login(request):
    if request.method == "POST":
        username_or_email = request.POST.get('username_or_email')  # Capture either username or email
        password = request.POST.get('password')

        # Check if the input is a valid email address using regex
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        user = None

        if re.match(email_regex, username_or_email):  # If it's a valid email
            try:
                user = User.objects.get(email=username_or_email)
            except User.DoesNotExist:
                pass  # Ignore if no user is found
        else:  # Else, treat it as a username
            user = User.objects.filter(username=username_or_email).first()

        # If a user is found, authenticate with the password
        if user:
            user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials.")
    
    return render(request, 'login.html')


def user_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                return redirect('/')
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, 'signup.html')


def forgot_password(request):
    return render(request, 'forgot_password.html')

from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def change_password(request):
    if request.method == "POST":
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Check if the old password is correct
        if not request.user.check_password(old_password):
            messages.error(request, "The old password is incorrect.")
            return render(request, 'change_password.html')

        # Check if the new password and confirm password match
        if new_password != confirm_password:
            messages.error(request, "The new password and confirm password do not match.")
            return render(request, 'change_password.html')

        # Update password
        if new_password:
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)  # Keep the user logged in after password change
            messages.success(request, "Your password has been successfully updated.")
            return redirect('dashboard')

    return render(request, 'change_password.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

def user_logout(request):
    logout(request)
    return redirect('login')

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        
        # Check if the email exists in the system
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "No account is associated with this email address.")
            return render(request, 'forgot_password.html')
        
        # Generate the reset token
        token = default_token_generator.make_token(user)
        
        # Send the reset email
        reset_url = request.build_absolute_uri(f"/reset_password/{user.username}/{token}/")
        subject = "Password Reset Request"
        message = f"Click the link below to reset your password:\n{reset_url}"
        send_mail(subject, message, 'transfinitetesting@gmail.com', [email])
        
        messages.success(request, "Password reset link has been sent to your email address.")
        return redirect('login')

    return render(request, 'forgot_password.html')

from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def reset_password(request, username, token):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        messages.error(request, "Invalid reset link.")
        return redirect('login')

    if not default_token_generator.check_token(user, token):
        messages.error(request, "Invalid or expired token.")
        return redirect('login')

    if request.method == "POST":
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been reset successfully.")
            return redirect('login')
    else:
        form = SetPasswordForm(user)

    return render(request, 'reset_password.html', {'form': form})
