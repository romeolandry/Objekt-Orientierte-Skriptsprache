from django.forms import *
from Studierendenverwaltung.models import *


class StudenForm(ModelForm):

    class Meta:
        model = Studierenden
        fields = ['vorname', 'nachname', 'email']


