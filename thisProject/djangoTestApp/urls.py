from django.conf.urls import url
# . indica dir actual
from . import views

urlpatterns = {
    #$ significa epieza con y termina con
    #cualquier cosa que pongamos entre ^s conicidirá
    #La raiz
    url(r'^$', views.index, name='index')
    #Tenemos que definir index en views.py

}
