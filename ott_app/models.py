from django.db import models
from admin_app.models import *

class Register(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone = models.CharField(max_length = 20)
    password = models.CharField(max_length = 25)


class Subscribed(models.Model):
    uid = models.ForeignKey(Register,on_delete = models.CASCADE)
    plan_id = models.ForeignKey(Subscription,on_delete = models.CASCADE)
    expiry = models.DateField()
    status = models.CharField(max_length = 30, default = 'inactive' )