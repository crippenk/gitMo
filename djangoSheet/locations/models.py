from django.db import models

# Create your models here.
class locations(models.Model):
    doctors_id = models.IntegerField(null=True, blank=True)
    clock_in = models.DateTimeField(null=True, blank=True)
    clock_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.doctors_id + self.clock_in + self.clock_out