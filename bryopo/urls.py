from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='mainpage'),
    # path('<str:str>/<slug:slug>', views.opo, name='opo'),
    # path('newsletter', views.newsletter, name='newsletter'),
    # path('newsletter/wyslany', views.newsletter_wysalny, name='newsletter_sent'),
    # path('bry/emaile', views, name='bry_emaile')
]

# article_detail(request, str="zakalec", slug="o-etruskach")
