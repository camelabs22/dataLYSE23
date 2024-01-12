
from django.urls import path
from datalyse import views

urlpatterns = [
    path('', views.sign_up),
    path('signin', views.sign_up),
    path('<str:email>', views.display, name='analysed'),
]