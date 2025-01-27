from help.common.a import A as HELP
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from user.serializers.CUSTOM import serializer as CSRLZR_USER


def landing(request):
    user = request.user
    html_path = 'landing/landing.html'
    context = {}
    if user.is_authenticated:
        context.update({
            'title': 'Daily Life' + f'({user.first_name})' if user.first_name else '',
            'navbar':  HELP().getNavbar(user, 2),
            'user': CSRLZR_USER.Usersrlzr(user, many=False).data,
        })
    else:
        context.update({
            'title': 'Daily Life',
            'navbar': HELP().getNavbar(user, 2),
        })
    return render(request, html_path, context=context)