from django.db import models
from django.db.models.fields import CharField

# class food(models.Model):
#     name= models.CharField(primary_key=True,max_length=150)
#     price=models.FloatField()
#     des=models.TextField()
#     cuisine=models.CharField(max_length=150)
#     chk1=models.BooleanField(default=False)
#     chk2=models.BooleanField(default=False)
#     chk3=models.BooleanField(default=False)
#     dat=models.DateField(auto_now=True)
#     radio=models.CharField(max_length=150)
#     img=models.FileField(upload_to='pic')
#     class Meta:  
#         db_table = "blooddonaton"

class blooddonation(models.Model):
    name= models.CharField(primary_key=True,max_length=150)
    age=models.FloatField()
    weight=models.FloatField()
    # des=models.TextField()
    bloodgroup=models.CharField(max_length=20)
    chk1=models.BooleanField(default=False)
    chk2=models.BooleanField(default=False)
    chk3=models.BooleanField(default=False)
    chk4=models.BooleanField(default=False)
    dat=models.DateField(auto_now=True)
    radio=models.CharField(max_length=150)
    img=models.FileField(upload_to='pic')
    class Meta:  
        db_table = "blooddonation"