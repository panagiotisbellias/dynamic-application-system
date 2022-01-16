from django import forms

class ApplicationForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_job = forms.CharField(label='Your job', max_length=400)
    headline = forms.CharField(label='Headline', max_length=200)
    content = forms.CharField(label='Content', max_length=800)