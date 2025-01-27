from rest_framework import serializers
from task import models as M_TASK
from user.serializers.GET import serializer as GSRLZR_USER

class Tasktypesrlzr(serializers.ModelSerializer):
    user=GSRLZR_USER.Usersrlzr(many=False)
    class Meta:
        model=M_TASK.Tasktype
        fields=['id', 'user', 'type', 'is_active']

class Tasksrlzr(serializers.ModelSerializer):
    type=Tasktypesrlzr(many=False)
    class Meta:
        model=M_TASK.Task
        fields=['id', 'type', 'description', 'task_datetime', 'is_complete', 'created_datetime', 'is_active']