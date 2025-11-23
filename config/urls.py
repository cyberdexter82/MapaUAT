from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.inicio_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('recuperar/', views.recuperar_view, name='recuperar'),
    path('logout/', views.logout_view, name='logout'),

    path('instrucciones/', views.instrucciones_view, name='instrucciones'),
    path('invitado/', views.invitado_view, name='invitado'),
    path('mapa/', views.mapa_view, name='mapa'),
]