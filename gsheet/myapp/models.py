from django.db import models

# Create your models here.
class Googs(models.Model):

    def __str__(self):
        return self.Ethnicity
    Ethnicity = models.CharField(max_length=100)
    Location = models.CharField(max_length=200)
    From = models.CharField(max_length=100)