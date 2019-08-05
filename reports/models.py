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
	content = HTMLField('Content')
	created = models.DateField(auto_now_add=True, db_index=True)
	users_liked = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='reports_liked', blank=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Report, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('reports:detail', args=[self.id, self.slug])

class Comment(models.Model):
	report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=500)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return 'Comment by {} on {}'.format(self.name, self.report)