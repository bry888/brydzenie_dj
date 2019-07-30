from django.urls import path

from . import views

app_name = 'bryopo'
urlpatterns = [
    path('', views.main, name='mainpage'),
    path('<str:str>/<slug:slug>', views.opo_chosen, name='opo_chosen'),
    path('newsletter', views.newsletter, name='newsletter'),
    path('newsletter/wyslany', views.newsletter_wysalny, name='newsletter_sent'),
    path('bry/emaile', views.bry_emaile, name='bry_emaile')
]

# article_detail(request, str="zakalec", slug="o-etruskach")
# <a href="{% url 'bryopo:mainpage' opo.id%}">{{ opo.json_text }}</a>
