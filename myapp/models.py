from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    dob = models.DateField()
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    medical_history = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Doctor(models.Model):
    full_name = models.CharField(max_length=80)
    doctorid = models.IntegerField(max_length=30)
    age = models.IntegerField()
    department = models.CharField(max_length=80)

    def __str__(self):
        return self.full_name

    #ward model , name, capacity department, floor

class Ward(models.Model):
    ward_name= models.CharField(max_length=80)
    capacity = models.IntegerField()
    department = models.CharField(max_length=80)
    floor = models.IntegerField()

    def __str__(self):
        return self.ward_name


class Appointment(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.IntegerField(max_length=80)
    datetime = models.DateTimeField()
    department = models.CharField(max_length=80)
    doctor = models.CharField(max_length=80)
    message = models.TextField()

    def __str__(self):
        return self.name
class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    subject = models.CharField(max_length=80)
    message = models.TextField()

    def __str__(self):
        return self.name

