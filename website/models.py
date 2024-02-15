from django.db import models

# Create your models here.
class Quotation(models.Model):
    home_appliances_choice = [
    ('Refrigerator', 'Refrigerator'),
    ('Stove with Oven', 'Stove with Oven'),
    ('Oven', 'Oven'),
    ('Dish Washer', 'Dish Washer'),
    ('Washer', 'Washer'),
    ('Dryer', 'Dryer'),
]
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    home_appliance = models.CharField(max_length=15, choices=home_appliances_choice)
    home_appliance_maker = models.CharField(max_length=15)
    home_appliance_model_number = models.CharField(max_length=30)
    home_appliance_problem = models.TextField()
    
    def __str__(self) -> str:
        return self.first_name
    
    
class ContactInfo(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.first_name
    
    
    
    
    
