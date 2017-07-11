from django.db import models


# Create your models here.cd

class Studierenden(models.Model):
    vorname = models.CharField(max_length=30)
    nachname = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    def __str__(self):
        return ("{} {} ".format(self.vorname, self.nachname))

class Lehveranstaltungen(models.Model):
    Kurzname = models.CharField(max_length=30)
    Title = models.CharField(max_length=30)
    studierenden = models.ManyToManyField(Studierenden)

    def __str__(self):
        return self.Title

class Lehver_Studierende(models.Model):
    student = models.ForeignKey(Studierenden)
    lehveranstaltung = models.ForeignKey(Lehveranstaltungen)

