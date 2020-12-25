from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    demo_content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})


    def save(self, *args, **kwargs):
        
        if len(self.content) > 101:
            self.demo_content = self.content[0:100] + '...'
        else:
            self.demo_content = self.content
        super(Post, self).save(*args, **kwargs)