from help.common.a import A as HELP
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.serializers.CUSTOM import serializer as CSRLZR_USER

@login_required
def profile(request, username=None):
    user = request.user
    html_path = 'error/error.html'
    context = {}
    if user.username == username:
        if user.is_authenticated:
            context.update({
                'is_authenticated': True,
                'title': user.get_full_name(),
                'navbar': HELP().getNavbar(user, 1),
                'user': CSRLZR_USER.Usersrlzr(user, many=False).data
            })
            html_path = 'user/profile/user_profile.html'
    else: context.update({'title': 'Page Not Found - Error'})

    return render(request, html_path, context=context)