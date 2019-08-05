from django.contrib import admin
from .models import Report, Comment
# Register your models here.

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'created']
	list_filter = ['created']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['name', 'report']