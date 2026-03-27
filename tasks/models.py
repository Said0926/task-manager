from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = [('todo', 'Не сделано'), ('in_progress', 'В работе'), ('done', 'Сделано')]

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    
    
    def __str__(self):
        return self.name