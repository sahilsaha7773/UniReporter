from django import forms
from django.contrib.auth.models import User
from .models import Report, Comment
from tinymce import TinyMCE

class ReportCreateForm(forms.ModelForm):
	content = forms.CharField(widget=TinyMCE(mce_attrs={'width': 800}))
	class Meta:
		model = Report
		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.fields['content'].widget.attrs.update(TinyMCE(mce_attrs={'width': 800}))
		fields = ('title', 'content')
		
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')

		def __init__(self, *args,**kwargs):
			super(CommentForm, self).__init__(*args, **kwargs)
			for visible in self.visible_fields():
				visible.field.widget.attrs['class'] = 'form-control'
