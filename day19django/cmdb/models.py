from django.db import models

# Create your models here.
class UserInfo(models.Model):
    # 默认会自动创建id列，自增，主键

    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)