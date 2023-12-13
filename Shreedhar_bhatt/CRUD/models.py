from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    notes = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)


    def _str_(self):
        return self.name
