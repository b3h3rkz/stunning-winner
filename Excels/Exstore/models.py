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
        # unique_together = ('first_name', 'last_name', 'age', 'gender', 'address',)

    def __str__(self):
        return self.fullname()

    def fullname(self):
        return self.first_name + self.last_name


class Log(models.Model):
    LOG_ACTIONS = (
        ('file_upload', 'file_upload'),
    )
    action = models.CharField(max_length=20, default='file_upload', choices=LOG_ACTIONS, verbose_name= 'action')
    message = models.CharField(max_length=200, default='nothing')
    date = models.DateTimeField(auto_now_add=True, verbose_name='date')

    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'