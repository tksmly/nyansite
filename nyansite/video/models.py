from django.db import models

# Create your models here.

class CreateUpdate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        #抽象类,不创建数据库
        abstract = True

class Video(CreateUpdate):
    video = models.FileField()
    title = models.CharField(max_length=50)