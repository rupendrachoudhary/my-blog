from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
	STATUS=(
		(0,'draft'),
		(1,'publish'),
		)
	title=models.CharField(max_length=200, unique=True)
	content=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True, null=True)

	#When you define a foreign key or many-to-many relations to the user model,
	#you should specify the custom model using the AUTH_USER_MODEL setting.
	#https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#substituting-a-custom-user-model
	#https://learndjango.com/tutorials/django-best-practices-referencing-user-model
	author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	status=models.IntegerField(choices=STATUS)

	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title