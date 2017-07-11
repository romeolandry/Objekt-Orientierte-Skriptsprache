from django.forms import *
from Studierendenverwaltung.models import *


class LehveranstaltungForm(ModelForm):

    class Meta:
        model = Lehveranstaltungen
        fields = ['Kurzname','Title']


