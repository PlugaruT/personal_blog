from django.db import models

# Create your models here.
class Article(models.Model):

	title = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	pub_date = models.DateField()
	content = models.TextField()
	image_url = models.TextField()
	image_url_preview = models.TextField()

	def __str__(self):
		return self.title + ' ' + str(self.pub_date)
