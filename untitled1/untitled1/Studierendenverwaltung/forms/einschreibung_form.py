from django.forms import *
from Studierendenverwaltung.models import *


class EinschreibungForm(ModelForm):

    class Meta:
        model = Lehveranstaltungen
        fields = ['studierenden']


