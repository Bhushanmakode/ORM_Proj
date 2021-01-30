from django.db import models

# Create your models here.
class Fakedata(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    job = models.CharField(max_length=30)
    salary = models.FloatField()
    city = models.CharField(max_length=30)
    dob = models.DateField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name