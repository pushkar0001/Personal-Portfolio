from django.db import models

# Create your models here
class Blog(models.Model):
    title = models.CharField(max_length=180)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title