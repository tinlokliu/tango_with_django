from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = {
    path('about/',views.about, name='about'),
}