from django import forms
from django.contrib.auth.models import User
from .models import Report

class ReportCreateForm(forms.ModelForm):
	class Meta:
		model = Report
		fields = ('title', 'content')