from django.db import models

# Create your models here.

# Profile 추가 (회원가입시 추가 기입 사항)
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    addresscode = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=300, blank=True)