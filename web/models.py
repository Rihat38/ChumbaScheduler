from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tag(models.Model):
    title = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Case(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    start_time = models.DateTimeField()
    remind_time = models.DateTimeField()
    is_repeatable = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
