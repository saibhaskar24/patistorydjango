from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    name = models.CharField(max_length = 20)
    content = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Details(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length = 20)
    qrcode = models.CharField(max_length = 40)
    bloodgroup = models.CharField(max_length=6)
    def __str__(self):
        return self.uid

class Info(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    bp = models.IntegerField()
    illness1 = models.CharField(max_length=40)
    illness2 = models.CharField(max_length=40)
    vaccination1 = models.CharField(max_length=40)
    vaccination2 = models.CharField(max_length=40)
    bloodsugarlevel = models.IntegerField()
    def __str__(self):
        return self.uid

class Prescriptions(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    d = models.DateTimeField()
    medicine = models.CharField(max_length=40)
    qty = models.IntegerField()
    interval = models.IntegerField()
    def __str__(self):
        return self.uid

class Tests(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    d = models.DateTimeField()
    tname = models.CharField(max_length=40)
    pdf = models.IntegerField()
    def __str__(self):
        return self.uid