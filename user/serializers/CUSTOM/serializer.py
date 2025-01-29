from rest_framework import serializers
from help.common.a import A as HELP
from user import models as M_USER
from task import models as M_TASK


class Tasksrlzr(serializers.ModelSerializer):
    class Meta:
        model=M_TASK.Task
        fields=['id', 'type', 'description', 'task_datetime', 'is_complete', 'created_datetime', 'is_active']

class Tasktypesrlzrmthd(serializers.ModelSerializer):
    tasks=serializers.SerializerMethodField()

    def get_tasks(self, instance):
        tasktypes=instance.task_type.all()
        serializer = Tasksrlzr(instance=tasktypes, many=True)
        return serializer.data
class Tasktypesrlzr(Tasktypesrlzrmthd):
    class Meta:
        model=M_TASK.Tasktype
        fields=['id', 'tasks', 'icon', 'type', 'is_active']

class Coverphotosrlzr(serializers.ModelSerializer):
    class Meta:
        model =M_USER.Coverphoto
        fields=['id', 'user', 'image', 'is_active']

class Profilepicsrlzr(serializers.ModelSerializer):
    class Meta:
        model=M_USER.Profilepic
        fields=['id', 'user', 'image', 'is_active']

class Usersrlzrmthd(serializers.ModelSerializer):
    profilepic=serializers.SerializerMethodField()
    profilepics=serializers.SerializerMethodField()
    coverphoto=serializers.SerializerMethodField()
    coverphotos=serializers.SerializerMethodField()
    tasktypes=serializers.SerializerMethodField()
    
    def get_profilepic(self, instance):
        profilepic=HELP().getProfilePic(instance)
        serializer = Profilepicsrlzr(instance=profilepic, many=False)
        return serializer.data
    
    def get_profilepics(self, instance):
        profilepics=instance.profilepic_user.all()
        serializer = Profilepicsrlzr(instance=profilepics, many=True)
        return serializer.data
    
    def get_coverphoto(self, instance):
        coverphoto=HELP().getCoverPhoto(instance)
        serializer = Coverphotosrlzr(instance=coverphoto, many=False)
        return serializer.data
    
    def get_coverphotos(self, instance):
        coverphotos=instance.coverphoto_user.all()
        serializer = Coverphotosrlzr(instance=coverphotos, many=True)
        return serializer.data
    
    def get_tasktypes(self, instance):
        tasktypes=instance.tasktype_user.all()
        serializer = Tasktypesrlzr(instance=tasktypes, many=True)
        return serializer.data
class Usersrlzr(Usersrlzrmthd):
    class Meta:
        model=M_USER.User
        fields=['id', 'phone', 'gender', 'profilepic', 'profilepics', 'coverphoto', 'coverphotos', 'tasktypes']