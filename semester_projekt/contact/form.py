from django import  forms

class contactform (forms.Form):
    name = forms.CharField(required = False, max_length=100, help_text='100 charactars max.')
    email = forms.EmailField(required = True)
    comment = forms.CharField(required = True, widget = forms.Textarea)