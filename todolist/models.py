from django.db import models
from django.contrib.auth.models import User




'''
    Only Model created named as Tasks containing feilds showm below.
    As todo list does not have need to store data date wise in different fields,
    All tasks of all times will be stored and shown on one page.
    But all task instances created will have Created_date field.
'''


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    meetlink = models.URLField(null=True, blank=True)

    def  __str__(self):
        return self.title


    class Meta:
        ordering = ['complete']