from django.db import models

def cat_image_path(instance, filename):
    path, ext = filename[-5:].split('.', 1)
    return f"images/cats/{instance.name}.{ext}"

class Cat(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to=cat_image_path)
    created_time = models.DateTimeField(auto_now_add=True)
