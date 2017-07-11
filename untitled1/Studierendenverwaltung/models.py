from django.db import models


# Create your models here.cd

class Studierenden(models.Model):
    vorname = models.CharField(max_length=255)
    nachname = models.CharField(max_length=250)
    email = models.EmailField(blank=True)

    def __str__(self):
        return ("{} {} ".format(self.vorname, self.nachname))

class Lehveranstaltungen(models.Model):
    Kurzname = models.CharField(max_length=250)
    Title = models.CharField(max_length=250)
    studierenden = models.ManyToManyField(Studierenden)

    def __str__(self):
        return self.Title

