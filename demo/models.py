from django.db import models

class Contact(models.Model):
	name = models.CharField(
        max_length=100,)
	phone = models.CharField(max_length=20,)
	subject = models.CharField(
        max_length=100,)
	message = models.CharField(max_length=1000,)