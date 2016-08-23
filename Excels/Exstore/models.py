from django.db import models


class UserData(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(default='Male', choices=GENDER_CHOICES, max_length=6)
    address = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'User Data'

    def __str__(self):
        return self.fullname()

    def fullname(self):
        return self.first_name + self.last_name