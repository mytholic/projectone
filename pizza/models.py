from django.db import models

class PIZZA(models.Model):
    pizza=models.CharField(max_length=20)
    price=models.CharField(max_length=20)

# Create your models here.
class customer(models.Model):
    userid=models.CharField(max_length=20)
    email=models.CharField(max_length=20)


class order(models.Model):
    username=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    