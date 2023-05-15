from django.urls import path
from . import views

urlpatterns = [
    path('ajout', views.ajout),
    path('traitement/', views.traitement),
    path('liste/', views.liste),
    path('/affiche/<int:id>/',views.affiche),
    path('/update/<int:id>/',views.traitementupdate),
]