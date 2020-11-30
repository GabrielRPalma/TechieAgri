from django.db import models 

# My models for the database
class Information(models.Model):

    name = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    file_name = models.CharField(max_length = 100)

    def __str__(self):

        return self.file_name