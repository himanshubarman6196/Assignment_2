from django import forms
from .models import Detail,GetImageSearch


class DetailForm(forms.ModelForm):
	
	class Meta:
		model = Detail
		fields = ('name','url','phone_number')


class PostImageUrlForm(forms.ModelForm):

	class Meta:
		model = GetImageSearch
		fields = ('name','upload')