from django.db import models
# Create your models here.

class user(models.Model):
    user_id = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    specialization = models.TextField()
    ob_id = models.TextField()
    department_id = models.TextField()
    work_period = models.TextField()

    def __str__(self):
        return self.first_name + '\r\n' + self.last_name
