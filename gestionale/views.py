import datetime
from random import randint
import JsonResponse
from django.http import HttpResponse
from gestionale.models import Esame, Paziente


def index(request):
    p = Paziente()
    p.codice_fiscale = 'TEST'
    p.nome = 'Mario'
    p.cognome = 'Rossi'
    p.save()

    e = Esame()
    e.valore = randint(4,15)
    e.unita_misura = 'mg'
    e.paziente = p
    e.save()

    return HttpResponse("Ciao. Oggi piove")

def index2(request):
    esami = Esame.objects.filter(valore__gte=10)
    risultati = []
    for esame in esami:
        risultati.append({
            'esame_valore': esame.valore
            'codice_fiscale': esame.paziente.codice_fiscale
            })

    return JsonResponse(risultati, safe=False)