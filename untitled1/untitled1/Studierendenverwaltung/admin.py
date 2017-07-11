from django.contrib import admin

# Register your models here.

from Studierendenverwaltung.models import *

admin.site.register(Studierenden )
admin.site.register(Lehveranstaltungen)

