from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.id}번 의사 {self.name}'

class Patient(models.Model):
    name = models.CharField(max_length=20)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id}번 환자 {self.name}'