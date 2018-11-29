from django.db import models

# Create your models here.
class Person(models.Model):
    p_name = models.CharField(max_length=16)
    p_sex = models.BooleanField(default=False)
class IDCard(models.Model):
    id_num = models.CharField(max_length=32,unique=True)
    # on_delete=models的PROTECT属性可以直接指定主从表删除模式[当主表有级联数据的时候，直接删除主表会报错，必须先删掉从表数据才能对主表数据进行操作]
    # 还有SET_NULL SET_DEFAULT
    id_person = models.OneToOneField(Person,null=True,blank=True,on_delete=models.PROTECT)

# 数据库的继承
class Animal(models.Model):
    a_anme = models.CharField(max_length=32)
    # 添加抽象，这样就不会在数据库中产生它的映射
    # 如果不添加抽象会产生三张表，如果抽象只会产生两张表但是两张表都会带有父类的属性
    class Meta:
        abstract = True
class Cat(Animal):
    c_eat = models.CharField(max_length=32)
class Dog(Animal):
    d_eat = models.CharField(max_length=32)