from django.contrib.auth.models import AbstractUser 
from django.db import models 
import random
 
 
 
class CustomUser(AbstractUser): 
    pass 
 
 
#register model is here 
class Registration(models.Model):
    trade = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    registration_id = models.CharField(max_length=4, unique=True, primary_key=True)  # Unique 4-digit ID

    def save(self, *args, **kwargs):
        if not self.registration_id:
            # Generate a unique 4-digit ID
            unique_id = self.generate_unique_id()
            self.registration_id = unique_id
        super().save(*args, **kwargs)

    def generate_unique_id(self):
        while True:
            # Generate a random 4-digit number
            unique_id = str(random.randint(1000, 9999))
            # Check if the generated ID already exists in the database
            if not Registration.objects.filter(registration_id=unique_id).exists():
                return unique_id

    def str(self):
        return self.registration_id  # or any other field you want to represent the object
    
class Attendance(models.Model): 
    trade_name = models.CharField(max_length=100) 
    roll_number = models.CharField(max_length=50) 
    full_name = models.CharField(max_length=100)  # You might want to consider using a ForeignKey to a User model instead 
    # registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    attendance_status = models.CharField(max_length=50) 
    attendance_date = models.DateField(auto_now_add=True)  # Set to current date when the object is created 
    InTime = models.TimeField(auto_now_add=True,null=True, blank=True)  # Set to current time when the object is created 
    OutTime = models.TimeField(auto_now=True)  # Update with the current time whenever the object is updated 
    voice_points =  models.CharField(max_length=50,null=True, blank=True) # for voice
    face_points =  models.CharField(max_length=50,null=True, blank=True) # for face
    eye_points =  models.CharField(max_length=50,null=True, blank=True) # for eye
    # Other fields as needed 
 
 
 
 
#system info database store code  
class SystemInfo(models.Model): 
    mac_address = models.CharField(max_length=50) 
    public_ip_address = models.CharField(max_length=50) 
    local_ip_address = models.CharField(max_length=50) 
    latitude = models.FloatField(null=True, blank=True) 
    longitude = models.FloatField(null=True, blank=True) 
    trade = models.CharField(max_length=100,null=True, blank=True)  # Define the trade field 
    roll_number = models.CharField(max_length=50,null=True, blank=True)  # Define the roll_number field


# creating contact use form 
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name