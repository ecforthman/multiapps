from django import forms
from . import helpers


class CipherTextForm(forms.Form):
    #CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
    CHOICES = helpers.create_choices(26)
    title = forms.CharField(max_length=30)
    author = forms.CharField(max_length=30)
    cipher_key = forms.CharField(max_length=30)
    cipher_key_offset = forms.ChoiceField(choices=CHOICES)
    text = forms.CharField(
            max_length=2000,
            widget=forms.Textarea(attrs={'placeholder' : 'Enter readable text here'}) 
    )

    '''
    source = forms.CharField(            # A hidden input for internal use
             max_length=50,              # tell from which page the user sent the message
             widget=forms.HiddenInput()
    )
    '''


    def clean(self):
        cleaned_data = super(CipherTextForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('author')
        message = cleaned_data.get('text')
        if not name and not email and not message:
            raise forms.ValidationError('Form Errors!')