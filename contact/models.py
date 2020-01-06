from django.db import models

# Create your models here.
class MessageMe(models.Model):
    email = models.EmailField()
    subject= models.CharField(max_length=20)
    message = models.TextField()



    