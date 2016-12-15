from __future__ import unicode_literals

from django.db import models

# Create your models here.


class SafeBox(models.Model):
    git = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Key(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to='documents', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    safe_box = models.ForeignKey(SafeBox, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
