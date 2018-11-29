from django.db import models

# Create your models here.
class Icon(models.Model):
    name = models.CharField(max_length=64)
    # 可以设置年月日避免Linux系统中的65535个最大文件限制
    ico = models.ImageField(upload_to='%Y/%m/%d/img')