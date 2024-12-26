from django.contrib import admin
from task import models as M_TASK

admin.site.register([
    M_TASK.Tasktype,
    M_TASK.Task
])