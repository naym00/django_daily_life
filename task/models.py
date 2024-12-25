from django.db import models
from user import models as M_USER

class Tasktype(models.Model):
    user = models.ForeignKey(M_USER.User, on_delete=models.CASCADE, related_name='tasktype_user')
    type = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.is_active}'    
    
class Task(models.Model):
    user = models.ForeignKey(M_USER.User, on_delete=models.CASCADE, related_name='task_user')
    type = models.ForeignKey(Tasktype, on_delete=models.CASCADE, related_name='task_type')
    description = models.TextField(blank=True, null=True)
    task_datetime = models.DateTimeField()
    
    created_datetime = models.DateTimeField(auto_now_add=True)
    
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.is_active}'