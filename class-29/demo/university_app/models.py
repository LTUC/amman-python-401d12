from django.db import models

# Create your models here.
class University(models.Model):
    alpha_two_code = models.CharField(max_length=100, null=False, blank=False)
    web_pages = models.CharField(max_length=300, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=300, null=False, blank=False)
    state_province = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
