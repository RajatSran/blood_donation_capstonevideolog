from django.db import models
from multiselectfield import MultiSelectField
import datetime

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Patient(models.Model):
    genderTypes=(
        ('N','None'),
        ('M','Male'),
        ('F','Female'),
        ('O','Others')
    )
    facilities=(
        ('AC','Air conditioner'),
        ('PN','Personal Nurse'),
        ('PR','Personal Room'),
        ('FF','Food Facility'),
        ('DC','Doctor Concent')
    )
    fullname = models.CharField(db_column='Name',max_length=100)
    pat_code = models.CharField(max_length=3)
    contact= models.CharField(max_length=15)
    wardno= models.CharField(db_column='Ward No.',max_length=3,default='0')
    age=models.IntegerField(db_column='Age',default='0')
    gender=models.CharField(db_column='Gender',choices=genderTypes,max_length=128,default='N')
    Admit_Status=models.BooleanField(db_column='Admit Stataus',default='True')
    facility=MultiSelectField(db_column='Facilities',choices=facilities,default='DC')
    admitdate = models.DateField(db_column='Admit_Date') 
    address = models.TextField(db_column='Address')
    patientimg = models.ImageField(db_column='PImage',upload_to='',null=True)


    
