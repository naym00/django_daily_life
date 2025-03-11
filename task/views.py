from help.common.a import A as HELP
from task import models as M_TASK
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from task.serializers.CUSTOM import serializer as CSRLZR_TASK

@login_required
def task_list(request, id=None):
    user = request.user
    html_path = 'error/error.html'
    context = {}
    if user.is_authenticated:
        context.update({
            'is_authenticated': True,
            'title': 'Task - ' + user.get_full_name(),
            'navbar': HELP().getNavbar(user, 1),
            'tasks': None
        })
        tasktype = M_TASK.Tasktype.objects.filter(id=id)
        if tasktype.exists():
            tasks = tasktype.first().task_type.filter(is_active=True)
            if tasks.exists(): context['tasks'] = CSRLZR_TASK.Tasksrlzr(tasks, many=True).data
        html_path = 'task/task_list.html'

    return render(request, html_path, context=context)