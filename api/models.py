from django.db import models

# Create your models here.

class Company(models.Model):
    compny_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=50,choices=(('IT','IT'),('None It','None It'),('Mobile phones','Mobile Phones')))
    added_date=models.DateTimeField(auto_now=True)
    actived=models.BooleanField(default=True)

    def __str__(self):
        return self.name



# Empoly Model
class Empoly(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=(('manager','manager'),('softdeveloper','sd'),('team lead]rder','pl')))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)


