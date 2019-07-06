from django.db import models
from django.conf import settings
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Report(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reports_created', on_delete=models.CASCADE)
	title = models.CharField(max_length=1000)
	slug = models.SlugField(max_length=200, blank=True)
	url = models.URLField()
	content = HTMLField()
	created = models.DateField(auto_now_add=True, db_index=True)
	users_liked = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='reports_liked', blank=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Report, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('reports:detail', args=[self.id, self.slug])