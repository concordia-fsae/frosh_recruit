from django.db import models

# Create your models here.

class Team(models.Model):
    team_name = models.CharField("Team Name", max_length = 10)
    value = models.IntegerField("Value")

    def __str__(self):
        return self.team_name


class Form_Response(models.Model):
    first_name = models.CharField("First Name", max_length=30)
    last_name = models.CharField("Last Name", max_length=30)
    email = models.EmailField("Email Address", max_length=100)
    interests = models.ManyToManyField(Team, related_name="interests", blank=True)
    program = models.CharField("Program", max_length=20)
    year = models.IntegerField("Year")

    def __str__(self):
        return self.first_name + " " + self.last_name
