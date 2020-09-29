from django.db import models

# Create your models here.


class Logo(models.Model):
    title = models.CharField(null=False, max_length=20)
    logo = models.ImageField(upload_to ='media/images') 

    def __str__(self):
        return self.title