from lib2to3.pytree import Leaf

from django.forms import ModelForm,ModelMultipleChoiceField,Form,ChoiceField
from Studierendenverwaltung.models import *


class LehveranstaltungForm(ModelForm):

    class Meta:
        model = Lehveranstaltungen
        fields = ['Kurzname','Title']


class EinschreibungForm(ModelForm):

    class Meta:
        model = Lehveranstaltungen
        exclude = ['Kurzname','Title']

def get_my_choice ():
    Select_CHOICES = [[lehver.id, lehver.Title] for lehver in Lehveranstaltungen.objects.all()]
    return  Select_CHOICES


class SelectForm(Form):

    lehveranstaltung = ChoiceField(choices=get_my_choice())

    # def __init__(self, *args, **kwargs):
    #     super(SelectForm,self).__init__(*args,**kwargs)
    #     self.fields['Title'] = ChoiceField(choices = get_my_choice())

    #select = ModelMultipleChoiceField(choices=Select_CHOICES, widget=ModelMultipleChoiceField,queryset=Lehveranstaltungen.objects.all() ,required=False)
   