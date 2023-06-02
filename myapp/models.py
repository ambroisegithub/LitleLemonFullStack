from django.db import models

# Create your models here.
class MenuItem(models.Model):
    first_name = models.CharField(max_length=255)
    reservation_data = models.DateField(max_length=255)
    reservation_slot = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.first_name
            
    
    