from django.db import models

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=200)
    #accreditation = models.CharField(max_length=20)
    #health_care_provider_type = models.CharField(max_length=20)
    registration_number = models.IntegerField()
    address = models.TextField()
    phone_number = models.IntegerField(max_length=15)
    website = models.URLField()