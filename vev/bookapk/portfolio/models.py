from django.db import models

class intouch(models.Model):
        name=models.CharField(max_length=100)
        phone=models.CharField(max_length=20)
        email=models.EmailField(default='email@example.com')
        message=models.TextField()

        def __str__(self):
                return 'message from '+self.name+'-'+self.email
                

        def __str__(self):
             return 'customer: '+self.name+'-'+self.email
from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=100)