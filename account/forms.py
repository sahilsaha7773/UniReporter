from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')
		# helper = FormHelper()
		# helper.form_class = 'form-group'
		# helper.layout = Layout(
	 #        Field('username', css_class='form-control'),
	 #        Field('first_name', rows="3", css_class='form-control'),
	 #        Field('email', css_class='form-control'),
	 #   	)

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match')
		return cd['password2']

class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email') 

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('date_of_birth', 'photo')