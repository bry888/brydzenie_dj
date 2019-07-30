from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Emaile, Oposy

def main(request):
    opowiadania = Oposy.objects.order_by('-year_added')
    najnowsze = opowiadania.filter(year_added='2019')
    zartem = opowiadania.filter(opo_cat='zartem')
    return render(request, 'bryopo/index.html', {'najnowsze': najnowsze, 'zartem': zartem})

def opo_chosen(request, str, slug):
    opowiadanie = get_object_or_404(Oposy, opo_name=slug)
    return render(request, 'bryopo/opo.html', {'opowiadanie': opowiadanie})


def newsletter(request, email):
    try:
        new_email = email.choice_set.get(pk=request.POST['email'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('bryopo:newsletter_sent'))

def newsletter_wysalny(request):
    return HttpResponseRedirect(reverse('bryopo:newsletter_sent'))

def bry_emaile(request):
    lista_emaili = Emaile.objects.order_by('created')
    output = ', '.join([e.email for e in lista_emaili])
    return HttpResponse(output)


# https://docs.djangoproject.com/en/2.2/topics/templates/
