from django.db import models

# Create your models here.


class Doctors(models.Model):
    doctors_id = models.IntegerField()
    first_name = models.CharField('First', max_length=50)
    last_name = models.CharField('Last', max_length=50)
    specialization = models.TextField()
    ob_id = models.IntegerField()
    department_id = models.IntegerField()
    work_period = models.IntegerField()

    def __str__(self):
        return self.last_name
