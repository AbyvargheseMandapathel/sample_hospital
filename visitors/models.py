from django.db import models

class Meta:
    app_label = 'visitors'

class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name  # Display the doctor's name in the admin interface

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.name  # Display the doctor's name in the admin interface

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    token_number = models.IntegerField(default=0)
    def __str__(self):
        return self.name  # Display the doctor's name in the admin interface
    
class DoctorToken(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    token_number = models.IntegerField(default=0)
    def __str__(self):
        return self.token_number  # Display the doctor's name in the admin interface
