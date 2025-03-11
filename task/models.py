from django.db import models
from user import models as M_USER
from help.common.a import A as HELP

def upload_tasktype_icon(instance, filename):
    if filename[-4:] == '.jpg':
        return "files/user/{username}/tasktype/{unique}.jpg".format(username=instance.user.username, unique=HELP().uniqueNumber())

class Tasktype(models.Model):
    user = models.ForeignKey(M_USER.User, on_delete=models.CASCADE, related_name='tasktype_user')
    type = models.CharField(max_length=50, unique=True)
    icon = models.ImageField(upload_to=upload_tasktype_icon, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.type} - {self.user.username} - {self.is_active}'
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    
class Task(models.Model):
    title = models.CharField(max_length=50, unique=True)
    type = models.ForeignKey(Tasktype, on_delete=models.CASCADE, related_name='task_type')
    description = models.TextField(blank=True, null=True)
    task_datetime = models.DateTimeField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.is_active}'
    
class Taskinfo(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='taskinfo_task')
    description = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.is_complete}'