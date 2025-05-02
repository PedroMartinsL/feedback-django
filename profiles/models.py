from django.db import models

# Create your models here.
class UserProfile(models.Model):
    image = models.ImageField(upload_to='images')#will not be saved in the database, but will be saved in the media folder
    #images folder inside of the uploads folder