from django.db import models

# Create your models here.

class Department(models.Model):  
    id = models.BigAutoField(primary_key=True)  
    name = models.CharField(max_length=100)     
    desc = models.TextField()      

    def __str__(self):             
        return self.name
    

class Doctor(models.Model): 
    id = models.BigAutoField(primary_key=True)  
    name = models.CharField(max_length=200)     
    spec = models.TextField()     
    dep_name = models.ForeignKey(Department, on_delete = models.CASCADE)     
    doc_image = models.ImageField(upload_to='doctors', default='default_image.jpg')      

    def __str__(self):             
        return 'Dr' +". "+ self.name  
    

class Booking(models.Model):

    id = models.BigAutoField(primary_key=True)    
    name = models.CharField(max_length=255,default='')    
    phone = models.CharField(max_length=10,default='')    
    email = models.EmailField(max_length=50,default='')    
    dep_name = models.ForeignKey(Department, on_delete = models.CASCADE)     
    doc_name = models.ForeignKey(Doctor, on_delete = models.CASCADE)     
    booking_date = models.DateField(null=True )
    booked_on = models.DateField(null=True )
    description = models.TextField(default='')

    def __str__(self):             
        return self.name