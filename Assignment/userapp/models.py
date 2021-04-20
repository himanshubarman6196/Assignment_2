from django.db import models
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Detail(models.Model):
    name  		 = models.CharField(max_length=100,blank=False,null=True)
    url   		 = models.URLField(max_length = 200, blank=False)
    phone_number = PhoneNumberField(unique=True)
    # phone_number = PhoneField(blank=False, help_text='Contact phone number')

class GetImageSearch(models.Model):
	name  		 = models.CharField(max_length = 200, blank=False,null=True)
	upload 		 = models.ImageField(upload_to ='uploads/')
	date_added   = models.DateTimeField(auto_now_add=True)


class ShowImage(models.Model):
	show_image = models.BooleanField(default=False)


