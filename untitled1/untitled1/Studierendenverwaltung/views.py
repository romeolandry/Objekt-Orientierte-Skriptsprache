from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse_lazy

from Studierendenverwaltung.forms.lehveranstaltung_form import LehveranstaltungForm
from Studierendenverwaltung.forms.studen_form import *
from Studierendenverwaltung.models import *
from Studierendenverwaltung.forms.einschreibung_form import *
from django.views.generic import DeleteView, UpdateView


# Create your views here.

def studierenden_list (request):
    return render_to_response(
        'studierenden/studirenden_list.html',
        {'page_title': 'Studierenden',
         'studirendens': Studierenden.objects.all()
         }
    )

def studierenden_new (request, pk = None):

    page_title = 'Studierende hinzufügen'
    studen = Studierenden()
    success_msg = 'Studierende hinzugefügt'
    if request.method == 'GET':
        form = StudenForm(instance=studen)

    else:
        form = StudenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/studierende')
        else:
            form = StudenForm(instance=studen)

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
        success_msg = 'studierende erfolgreich geändert !'
    if (request.method == 'GET'):
        print('test du GET')
        form = StudenForm(instance=studen)

    else:
        form = StudenForm(request.POST, instance=studen)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/studierende')
        else:
            form = StudenForm(instance=studen)

    return render(request, 'studierenden/student.html',
                  {'page_title': page_title,
                   'form': form,
                   }
                  )

def studierenden_delete (request, pk = None):

    if pk:
        page_title = 'Student loeschen'
        studen = get_object_or_404(Studierenden, pk=pk)
        success_msg = 'studierende erfolgreich geloescht !'

    if request.method == 'GET':
        print('Get :'+ pk)
        form = StudenForm(instance=studen)

    else:
        form = StudenForm(request.POST, instance=studen)
        if form.is_valid():
            studen.delete()
            return HttpResponseRedirect('/studierende')

            # model = Studierenden
            # return HttpResponseRedirect('/studierende')
        else:

            form = StudenForm(instance=studen)

    return render (request, 'studierenden/student.html',
                   {'page_title' : page_title,
                    'form':form,
                    }
                   )
#---------------------------------------------------------------------------
#veranstaltung
#----------------------------------------------------------------------------

def lehveranstaltung_list (request):
    print(Lehveranstaltungen.objects.all())
    print(Lehveranstaltungen.studierenden)
    return render_to_response(
        'lehveranstaltung/lehveranst_list.html',
        {'page_title': 'Lehveranstaltungen',
         'lehveranstaltungs': Lehveranstaltungen.objects.all()
         })

def lehveranstaltung_new (request):

    page_title = 'Lehveranstaltung hinzufügen'
    leveranstaltung = Lehveranstaltungen()
    success_msg = 'Lehveranstaltung  hinzugefügt'
    if request.method == 'GET':
        form = LehveranstaltungForm(instance=leveranstaltung)

    else:
        form = LehveranstaltungForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success_msg = 'Lehveranstaltung  hinzugefügt'
            return HttpResponseRedirect('/lehveranstaltung')
        else:
            form = LehveranstaltungForm(instance=leveranstaltung)

    return render (request, 'lehveranstaltung/lehveranstaltung.html',
                   {'page_title' : page_title ,
                    'form':form,
                    }
                   )

def lehveranstaltung_edit (request, pk = None):

    if pk:
        print('test du pk')
        page_title = 'lehveranstaltung ändern'
        leveranstaltung = get_object_or_404(Lehveranstaltungen, pk=pk)
        success_msg = 'lehveranstaltung erfolgreich geändert !'

    if (request.method == 'GET'):
        print('test du GET')
        form = LehveranstaltungForm(instance=leveranstaltung)

    else:
        form = LehveranstaltungForm(request.POST, instance=leveranstaltung)
        if form.is_valid():
            form.save()
            success_msg = 'lehveranstaltung erfolgreich geändert !'
            return HttpResponseRedirect('/lehveranstaltung')
        else:
            form = LehveranstaltungForm(instance=leveranstaltung)

    return render(request, 'lehveranstaltung/lehveranstaltung.html',
                  {'page_title': page_title,
                   'form': form,
                   }
                  )

def lehveranstaltung_delete (request, pk = None):

    if pk:
        page_title = 'lehveranstaltung loeschen'
        leveranstaltung = get_object_or_404(Lehveranstaltungen, pk=pk)
        success_msg = 'lehveranstaltungerfolgreich geloescht !'

    if request.method == 'GET':
        print('Get :'+ pk)
        form = LehveranstaltungForm(instance=leveranstaltung)

    else:
        form = LehveranstaltungForm(request.POST, instance=leveranstaltung)
        if form.is_valid():
            leveranstaltung.delete()
            success_msg = 'lehveranstaltungerfolgreich geloescht !'
            return HttpResponseRedirect('/lehveranstaltung')

            # model = Studierenden
            # return HttpResponseRedirect('/studierende')
        else:

            form = LehveranstaltungForm(instance=leveranstaltung)

    return render (request, 'lehveranstaltung/lehveranstaltung.html',
                   {'page_title' : page_title,
                    'form':form,
                    }
                   )

#___________________________________________________________________________________________
#----------------------- Einschreibung---------------------------------
#___________________________________________________________________________________________
def studierenden_enschreiben(request, pk=None):
    if pk:
        page_title = 'Sechreiben Sie sich ein!'
        leveranstaltung = get_object_or_404(Lehveranstaltungen, pk=pk)
        list_studen =leveranstaltung.studierenden.all()
        print(list_studen)
        form = EinschreibungForm(instance=leveranstaltung)
    if request.method == 'GET':
        print('Get :'+ pk)
        form = EinschreibungForm(instance=leveranstaltung)
    else:
        form = EinschreibungForm(request.POST, instance=leveranstaltung)
        if form.is_valid():
            form.save()
            lehver = Lehveranstaltungen()
            lehver.studierenden.add(list_studen)
            success_msg = 'Sie sind erfohreich eingeschrieben !'
            return HttpResponseRedirect('/lehveranstaltung')

            # model = Studierenden
            # return HttpResponseRedirect('/studierende')
        else:
            form = LehveranstaltungForm(instance=leveranstaltung)
    return render(request,
                  'einschreibung/einschreibung.html',
                  {'page_title': page_title,
                   'form': form
                   })

# def studierenden_enschreiben(request, pk=None):
#     student_id = None
#     if pk:
#         student_id = pk
#         page_title = 'Sechreiben Sie sich ein!'
#         studen = Studierenden()
#         if request.method == 'GET':
#             # print('Get :'+ pk)
#             # form = EinschreibungForm(instance=studen)
#             list_Lehver = Lehveranstaltungen.objects.all()
#             print(list_Lehver)
#             form = StudenForm(instance=studen)
#             return render(request,
#                           'einschreibung/St_Einschreibung.html',
#                           {'page_title': page_title,
#                            'list_lehver': list_Lehver,
#                            })
#
#     # else:
#     #     # form = EinschreibungForm(request.POST, instance=studen)
#     #     # if form.is_valid():
#     #     #     form.save()
#     #     #     success_msg = 'Sie sind erfohreich eingeschrieben !'
#     #     #     return HttpResponseRedirect('/lehveranstaltung')
#     #     pass
#     #         # model = Studierenden
#     #         # return HttpResponseRedirect('/studierende')
#     #     else:
#     #         # form = LehveranstaltungForm(instance=studen)
#     #         pass
#     # # return render(request,
#     # #               'einschreibung/einschreibung.html',
#     # #               {'page_title': 'Wählen Sie die Fächer',
#     # #                'form': form
#     # #                })
#     # pass