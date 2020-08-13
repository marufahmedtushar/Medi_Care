from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


class Doctor(models.Model):
    doctor_id = models.AutoField
    registration_number = models.CharField(max_length=100)
    registration_type = models.CharField(max_length=100)
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    cover = models.ImageField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.registration_number


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    subject = models.CharField(max_length=70, default="")
    msg = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.first_name


class Prescription_pictures(models.Model):
    user_name = models.CharField(max_length=300)
    cover = models.ImageField(upload_to="prescription", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.user_name

    def delete(self, *args, **kwargs):
        self.cover.delete()
        super().delete(*args, **kwargs)  # Call the "real" save() method.


class Bloodds(models.Model):
    donner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    age = models.CharField(max_length=1000, default="")
    phone = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    bloodgroup = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=600, default="")
    lastdonate= models.DateField(("Date"), default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE ,default="")

    def __str__(self):
        return self.name

