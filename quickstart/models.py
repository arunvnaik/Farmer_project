from django.db import models
from django.core.validators import MinValueValidator

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Crop(models.Model):
    name = models.CharField(max_length=100)
    time_to_grow = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1)])
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='crops')

    def __str__(self):
        return self.name
        
class Earnings(models.Model):
    farmer = models.OneToOneField(Farmer, on_delete=models.CASCADE, related_name='earnings')
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='earnings')
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.farmer.name}'s earnings for {self.crop.name}"
