from pathlib import _Selector
from django.contrib import messages
from django.contrib.admin.utils import get_deleted_objects
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from pip._vendor.requests.api import request

from Studierendenverwaltung.models import *

from Studierendenverwaltung.forms.lehveranstaltung_form import *
from Studierendenverwaltung.forms.studen_form import *
from Studierendenverwaltung.models import *
from django.views.generic import DeleteView, UpdateView,CreateView


# Create your views here.

def studierenden_list (request):

    return render(request,
        'studierenden/studirenden_list.html',
        {'page_title': 'Studierenden',
         'studirendens': Studierenden.objects.all()
         }
    )

def studierenden_new (request, pk = None):

    page_title = 'Studierende hinzufügen'
    studen = Studierenden()
    if request.method == 'GET':
        form = StudenForm(instance=studen)

    else:
        form = StudenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, u'Studierende hinzugefügt')
            return HttpResponseRedirect(reverse_lazy('Studierenden'))

        else:
            messages.error(request, u'Prüfen sie Data')
            pass

    return render (request, 'studierenden/student.html',
                   {'page_title' : page_title ,
                    'form':form,
                    }
                   )


def studierenden_edit (request, pk = None):

    if pk:
        print('test du pk')
        page_title = 'Student ändern'
        studen = get_object_or_404(Studierenden, pk=pk)
    if (request.method == 'GET'):
        print('test du GET')
        form = StudenForm(instance=studen)

    else:
        form = StudenForm(request.POST, instance=studen)
        if form.is_valid():
            form.save()
            messages.success(request, u'studierende erfolgreich geändert !')
            return HttpResponseRedirect('/studierende')
        else:
            messages.error(request, u'Prüfen sie Data')

    return render(request, 'studierenden/student.html',
                  {'page_title': page_title,
                   'form': form,
                   }
                  )

def studierenden_delete (request, pk = None):

    if pk:
        page_title = 'Student loeschen'
        studen = get_object_or_404(Studierenden, pk=pk)

    if request.method == 'GET':
        print('Get :'+ pk)
        form = StudenForm(instance=studen)

    else:
        form = StudenForm(request.POST, instance=studen)
        if form.is_valid():
            studen.delete()
            messages.success(request, u'studierende erfolgreich geloescht !')
            return HttpResponseRedirect('/studierende')
        else:
            messages.error(request, u' Data wurde nicht korrect gelöscht')
            form = StudenForm(instance=studen)

    return render (request, 'studierenden/student.html',
                   {'page_title' : page_title,
                    'form':form,
                    }
                   )
#---------------------------------------------------------------------------
#Lehveranstaltung
#----------------------------------------------------------------------------

def lehveranstaltung_list (request):
    print(Lehveranstaltungen.objects.all())
    print(Lehveranstaltungen.studierenden)
    return render(request,
        'lehveranstaltung/lehveranst_list.html',
        {'page_title': 'Lehveranstaltungen',
         'lehveranstaltungs': Lehveranstaltungen.objects.all()
         })

def lehveranstaltung_new (request):

    page_title = 'Lehveranstaltung hinzufügen'
    leveranstaltung = Lehveranstaltungen()
    if request.method == 'GET':
        form = LehveranstaltungForm(instance=leveranstaltung)

    else:
        form = LehveranstaltungForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, u'Lehveranstaltung wurde erfolgreich hinzugefügt!')
            return HttpResponseRedirect('/lehveranstaltung')
        else:
            messages.error(request, u' Data wurde nicht korrect hinzugefügt')


    return render (request, 'lehveranstaltung/lehveranstaltung.html',
                   {'page_title' : page_title ,
                    'form':form,
                    }
                   )

def lehveranstaltung_edit (request, pk = None):

    if pk:

        page_title = 'lehveranstaltung ändern'
        leveranstaltung = get_object_or_404(Lehveranstaltungen, pk=pk)

    if (request.method == 'GET'):
        print('test du GET')
        form = LehveranstaltungForm(instance=leveranstaltung)

    else:
        form = LehveranstaltungForm(request.POST, instance=leveranstaltung)

        if form.is_valid():
            form.save()
            messages.success(request, u'Lehveranstaltung wurde erfolgreich geändert!')
            return HttpResponseRedirect('/lehveranstaltung')
        else:
            messages.error(request, u' lehveranstaltung wurde nicht korrect geändert')

    return render(request, 'lehveranstaltung/lehveranstaltung.html',
                  {'page_title': page_title,
                   'form': form,
                   }
                  )

def lehveranstaltung_delete (request, pk = None):

    if pk:
        page_title = 'lehveranstaltung loeschen'
        leveranstaltung = get_object_or_404(Lehveranstaltungen, pk=pk)

    if request.method == 'GET':
        print('Get :'+ pk)
        form = LehveranstaltungForm(instance=leveranstaltung)

    else:
        form = LehveranstaltungForm(request.POST, instance=leveranstaltung)
        if form.is_valid():
            leveranstaltung.delete()
            messages.success(request, u'Lehveranstaltung wurde erfolgreich gelöscht!')
            return HttpResponseRedirect('/lehveranstaltung')
        else:
            messages.error(request, u' lehveranstaltung wurde nicht korrect gelöscht')

    return render (request, 'lehveranstaltung/lehveranstaltung.html',
                   {'page_title' : page_title,
                    'form':form,
                    }
                   )

#___________________________________________________________________________________________
#----------------------- Einschreibung---------------------------------
#___________________________________________________________________________________________

def einschreibung_list(request, pk):

    print(Lehveranstaltungen.objects.all())
    if pk:
        page_title = 'Sechreiben Sie sich ein!'
        new_student = get_object_or_404(Studierenden, pk=pk)
        lehver = Lehveranstaltungen()

    if request.method == 'GET':
        form = SelectForm()
    else:
        lehrver = Lehveranstaltungen()
        form = SelectForm(request.POST)

        if form.is_valid():
            id_lehver= form.cleaned_data['lehveranstaltung']
            lehveranstaltung = get_object_or_404(Lehveranstaltungen, pk=id_lehver)
            find= False

            for std in lehveranstaltung.studierenden.all():
                if std.id == new_student.id:
                    find = True

            if find == True:
                messages.INFO(request, u'Sie sind schon eingeschrieben zu dieser Lehveranstaltung!')
                return HttpResponseRedirect('/lehveranstaltung')
            else:
                messages.info(request, u'Sie sind jetzt eingeschrieben zu dieser Lehveranstaltung!')
                lehveranstaltung.studierenden.add(new_student)
                return HttpResponseRedirect('/lehveranstaltung')


    return render(request,
        'einschreibung/einschreibung.html',
        {'page_title': 'Lehveranstaltungen',
         'form':form
         })