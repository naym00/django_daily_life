from help.common.a import A as HELP
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def userLogin(request):
    user = request.user
    html_path = 'authentication/login.html'
    context = {
        'title': 'Login',
        'navbar': HELP().getNavbar(user, 3),
        
        'errors': [],
        'username': '',
        'password': ''
    }
    if not user.is_authenticated:
        if request.method == 'POST':
            user_info = request.POST
            username = user_info.get('username')
            password = user_info.get('password')
            if username != None:
                if password != None:
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect(f'/user/profile/{username}')
                    else: context['errors'].append('Please provide valid credentials!')
                else: context['password'] = 'Password is Required!'
            else: context['username'] = 'Username is Required!'
    else: return redirect(f'/user/profile/{user.username}')
    return render(request, html_path, context=context)

@login_required
def userLogout(request):
    logout(request)
    return redirect(f'/')