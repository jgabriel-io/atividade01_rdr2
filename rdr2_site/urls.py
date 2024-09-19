from django.contrib import admin
from django.urls import path
from rdr2_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', views.sobre, name='sobre'),
    path('perfil/', views.perfil, name='perfil'),
    path('contato/', views.contato, name='contato'),
]
