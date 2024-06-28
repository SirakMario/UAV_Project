from django.db import models
from datetime import datetime
# Create your models here.

class Images(models.Model):
    image_choice = (
        ("RGB Orthomosaic", "RGB Orthomosaic"),
        ("Multispectral","Multispectral"),
        ("NDVI","NDVI"),
        ("Lidar","Lidar"),
        ("Change Detection", "Change Detection"),
        ("sfm","sfm"),
        ("DEM_DSM","DEM_DSM"),
        ("Diff_DEM_DSM_Volume","Diff_DEM_DSM_Volume")
    )
    
    name = models.CharField (max_length=100, blank=False)
    date = models.DateField(default= datetime.now)
    image_type = models.CharField (max_length= 20, choices=image_choice)
    description = models.TextField (blank=True)
    
    
    def __str__(self):
        return self.name
    
