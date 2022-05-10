from django.db import models
# Create your models here.

class workday(models.Model):
    workday_id = models.TextField()
    clock_in = models.TextField()
    clock_out = models.TextField()