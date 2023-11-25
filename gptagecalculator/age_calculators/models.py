from django.db import models
from django.contrib.auth.models import AbstractUser
from gptagecalculator.settings import AUTH_USER_MODEL

# Create your models here.
class User(AbstractUser):
    age = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = [age]

class Query(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL,on_delete=models.CASCADE)
    question = models.CharField(max_length=256,null=False,blank=True)
    answer = models.CharField(max_length=256,null=False,blank=True)
    event_age = models.DateTimeField()

    class Meta:
        db_table = 'user_query'
