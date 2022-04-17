from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    comments = models.TextField()

    def to_string(self):
        return  self.first_name + " " + self.last_name + " " + self.email + " " + self.comments
