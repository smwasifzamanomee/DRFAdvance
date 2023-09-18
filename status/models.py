from django.db import models
from django.contrib.auth.models import User

# Image upload Function
def upload_status_image(instance, filename):
    return "uploads/{user}/{filename}".format(user=instance.user, filename=filename)

# def upload_status_image(instance, filename):
#     return f"updates/{instance.user}/{filename}"

# Create your models here.
class Status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_status_image, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        # verbose_name = 'Status post'
        verbose_name_plural = 'Status List'
        # ordering = ['-created']
    
    def __str__(self):
        return str(self.content)[:20]
