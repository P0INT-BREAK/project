from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=get_email)  # Use email to get the user
            if user.check_password(get_password):  # Validate password
                auth_login(request, user)  # Log in the user
                messages.success(request, "Login successful")
                return redirect('/')  # Redirect to the homepage
            else:
                messages.error(request, "Invalid password")
        except User.DoesNotExist:
            messages.error(request, "Invalid email")
        
        return redirect('/auth/login')  # Redirect back to the login page on error
    
    return render(request, 'login.html')  # Render the login template

def logout_view(request):
    if request.user.is_authenticated:  # Check if the user is logged in
        auth_logout(request)  # Log out the user
        messages.success(request, "Logged out successfully")  # Add a success message
    else:
        messages.info(request, "You are not logged in")  # Optional: Inform if not logged in
    return redirect('/auth/login')  # Redirect to the login page or wherever you prefer