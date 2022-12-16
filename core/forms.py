from tinymce.widgets import TinyMCE
from django import forms

class NewsLetterForm(forms.Form):
    '''
    This form allows us to type HTML code
    From there we will be able to send our users their newsletters
    '''
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")

