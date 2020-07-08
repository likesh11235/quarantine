from django.db import models
from django.core.validators import EmailValidator
# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length = 20, help_text = "Enter your full name")
    gmail = models.EmailField(validators = ([EmailValidator]), blank = True, help_text = "optional")
    phoneNumber = models.IntegerField(unique = True, primary_key = True, help_text = "this num will be used to access your account")
    address = models.CharField(max_length = 100, help_text = "Enter your address")
    password = models.CharField(max_length = 20, help_text = "Enter strong Password")

    #to return in readable format
    def __str__(self):
        return self.name+" "+self.gmail+" "+str(self.phoneNumber)+" "+self.address