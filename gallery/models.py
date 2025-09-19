from django.db import models
from datetime import datetime
import os

#offers a return to upload_to to attach timestamp to filename
def photo_upload_to(instance, filename):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    base, ext = os.path.splitext(filename)
    new_filename = f"{timestamp}_{base}{ext}"
    return f'photos/{datetime.now().strftime("%Y/%m/%d")}/{new_filename}'

class Photograph(models.Model):
    
    CATEGORY_OPTIONS = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta"),
    ]


    title = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_OPTIONS, default='')
    description = models.TextField(null=True, blank=True)
    photo_path = models.ImageField(upload_to=photo_upload_to, blank=False)  # URL or path to the photo
    active = models.BooleanField(default=False)
    date_upload = models.DateField(default=datetime.now, blank=False)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=False, related_name='user')
    
    def __str__(self):
        return self.title