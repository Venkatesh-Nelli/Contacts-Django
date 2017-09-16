from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class contact_details(models.Model):
	user = models.ForeignKey(User)
	contact_name = models.CharField(max_length = 140)
	contact_number = models.IntegerField(default=0,validators=[MaxValueValidator(999999999999999)])
	contact_image = models.ImageField(upload_to='images/contact_images',blank=True)

	def __str__(self):
		return self.contact_name