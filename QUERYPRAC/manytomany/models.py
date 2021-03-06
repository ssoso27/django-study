from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.id}번 의사 {self.name}'

class Patient(models.Model):
    name = models.CharField(max_length=20)
    doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients') # Reservation을 통해서 담당 의사 목록 받아옴
    
    def __str__(self):
        return f'{self.id}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.doctor.id}번 의사의 {self.patient.id} 번 환자'