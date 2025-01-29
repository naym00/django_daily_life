from rest_framework import serializers
from task import models as M_TASK
from user.serializers.GET import serializer as GSRLZR_USER

class Tasksrlzr(serializers.ModelSerializer):
    class Meta:
        model=M_TASK.Task
        fields=['id', 'type', 'description', 'task_datetime', 'is_complete', 'created_datetime', 'is_active']

class Tasktypesrlzr(serializers.ModelSerializer):
    task_type=Tasksrlzr(many=True)
    user=GSRLZR_USER.Usersrlzr(many=False)
    class Meta:
        model=M_TASK.Tasktype
        fields=['id', 'user', 'task_type', 'icon', 'type', 'is_active']