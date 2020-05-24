from django.db import models

# Create your models here.
class Friend(models.Model):
    # NICK NAME should be unique
    email = models.CharField(max_length=100, unique =  True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length = 250)
    occupation = models.CharField(max_length=100, null = True, blank = True)
    lives_in = models.CharField(max_length=150, null = True, blank = True)

    def __str__(self):
        return self.email