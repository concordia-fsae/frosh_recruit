from django.db import models

# Create your models here.

class Form_Response(models.Model):
    first_name = models.CharField("First Name", max_length=30)
    last_name = models.CharField("Last Name", max_length=30)
    email = models.CharField("Email Address", max_length=100)
    interests = models.CharField("Interests", max_length=15)
    program = models.CharField("Program", max_length=20)
    year = models.IntegerField("Year")

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_interests(self):
        return self.interests
    
    def get_program(self):
        return self.program

    def get_year(self):
        return self.year