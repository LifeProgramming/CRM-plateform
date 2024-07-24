from django.db import models
from django.contrib.auth.models import User

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email =  models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address =  models.CharField(max_length=100)
    city =  models.CharField(max_length=50)
    state =  models.CharField(max_length=50)
    zipcode =  models.CharField(max_length=20)
    creator=models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self) :
        return self.name