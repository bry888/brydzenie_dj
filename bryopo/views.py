from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Emaile

def main(request):
    return HttpResponse("Hello, world. You're at the polls index.")




def newsletter(request):
    lista_emaili = Emaile.objects.order_by('created')
    output = ', '.join([e.email for e in lista_emaili])
    return HttpResponse(output)


# https://docs.djangoproject.com/en/2.2/topics/templates/
