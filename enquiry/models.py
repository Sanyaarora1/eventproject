from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    event_type = models.CharField(max_length=100)
    num_persons = models.IntegerField()
    preferred_location = models.CharField(max_length=200)
    event_date = models.DateField()
    requirements = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event_type}"