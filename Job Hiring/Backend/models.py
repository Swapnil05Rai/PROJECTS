from django.db import models

# Create your models here.
class Job(models.Model):
    Companyn= models.CharField(max_length=100)
    Jobtitle= models.CharField(max_length=100)
    Jobdescription= models.TextField()
    Joblocation= models.CharField(max_length=100)
