from rest_framework import serializers
from task import models as M_TASK

class Tasktypesrlzr(serializers.ModelSerializer):
    class Meta:
        model=M_TASK.Tasktype
        fields='__all__'

class Tasksrlzr(serializers.ModelSerializer):
    class Meta:
        model=M_TASK.Task
        fields='__all__'