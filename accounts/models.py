from django.db import models
from django.contrib.auth.models import User

#choices for models

GenderChoices = (
    ('N', 'None'),
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others'),
)

# Create your models here.
class UserPofile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    gender = models.CharField(max_length=20,null=True, blank=True, choices=GenderChoices,default=None)
    profile_pic = models.ImageField(upload_to='profile_pics', default='profile_pics/default.png')

    def __str__(self):
        return f'{self.user.username}`s profile'
