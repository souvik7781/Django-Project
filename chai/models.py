from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('BT', 'Black Tea'),
        ('CT', 'Classic Tea'),
        ('GT', 'Green Tea'),
        ('ET', 'Elaichi Tea'),
        ('LT', 'Lemon Tea'),
        ('MT', 'Masala Tea'),
    ]
    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
    def __str__(self):
        return self.name