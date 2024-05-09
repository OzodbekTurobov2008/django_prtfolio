from django.db import models


def str(self):
    return self.full_name


class Blog(models.Model):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="Blog/")


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length= 250)
    email = models.EmailField()
    subject = models.CharField(max_length= 5000)
    message = models.TextField()

def str(self):
    return self.name