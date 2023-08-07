from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import login
from django.shortcuts import redirect
# from social_django.views import OAuth2LoginView
from django.http import HttpResponse
import json


from privacy_guard_app.models import CustomUser

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = CustomUser.objects.create_user(email=email, username=username, password=password)
            messages.success(request, 'Registration successful. You can now log in.')
            # Automatically log in the newly registered user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('login')  # Replace 'dashboard' with your desired view name
        except IntegrityError:
            messages.error(request, 'Username or email already exists. Please try again with different credentials.')
        except Exception as e:
            messages.error(request, f'Registration failed: {e}')
        
        return redirect('register')

    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')

    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    
    return render(request, 'dashboard.html', {'user': request.user})


# Decorator for checking if the user is staff (admin)
def staff_required(view_func):
    decorated_view_func = login_required(user_passes_test(lambda u: u.is_staff))
    return decorated_view_func(view_func)

# Decorator for checking if the user is a superuser (admin with all permissions)
def superuser_required(view_func):
    decorated_view_func = login_required(user_passes_test(lambda u: u.is_superuser))
    return decorated_view_func(view_func)


def data(request):
    """Renders the page with the buttons."""

    if request.method == 'POST':
        email = request.POST['email']

        if request.POST['action'] == 'download_data':
            return download_data(request, email)
        elif request.POST['action'] == 'delete_data':
            return delete_data(request, email)

    return render(request, 'data.html')




def download_data(request, email=None):
    """Downloads the data for a user."""

    if not email:
        email = request.POST.get('email')

    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        return JsonResponse({'error': 'User does not exist.'})

    data = {
        'email': user.email,
        'username': user.username
    }

    response = HttpResponse(content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=user_data.json'
    response.write(json.dumps(data).encode('utf-8'))

    return response

def delete_data(request, email=None):
    """Deletes the data for a user."""

    if not email:
        email = request.POST.get('email')

    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        return JsonResponse({'error': 'User does not exist.'})

    user.delete()

    return JsonResponse({'success': 'Data deleted successfully.'})




# class GoogleLoginView(OAuth2LoginView):
#     """Handles the login process for Google SSO."""

#     provider_id = 'google'

#     def login(self, request, user, **kwargs):
#         """Logs the user in and redirects them to the dashboard page."""
#         login(request, user)
#         return redirect('dashboard')
