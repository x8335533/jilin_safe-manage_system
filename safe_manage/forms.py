from django import forms
from .models import Examination,Problem,Rectification,Comment,ImgProblem
from bootstrap_datepicker_plus import DateTimePickerInput

class ExaminationForm(forms.ModelForm):
	class Meta:
		model = Examination
		fields = ['datecheck','text']
		labels = {'datecheck':"检查日期",'text': '检查内容'}
		widgets = {'datecheck':DateTimePickerInput(
		options={"format": "YYYY-MM-DD","locale":"zh-cn",}),
		'text': forms.Textarea(attrs={'cols': 80}),
                 }

class ProblemForm(forms.ModelForm):
	class Meta:
		model = Problem
		fields = ['text']
		exclude = ['ifdone']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}
		
class ProblemPassForm(forms.ModelForm):
	class Meta:
		model = Problem
		fields = ['ifdone']
		exclude = ['text']
		labels = {'ifdone': '合格请确认'}

class RectificationForm(forms.ModelForm):
	class Meta:
		model = Rectification
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}
		
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}
		
class ImgProblemForm(forms.ModelForm):
	class Meta:
		model = ImgProblem
		fields = {'img'}
			
