from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('projeler/', views.ProjeView, name="proje"),
    path('projeler/<slug:slug>/', views.ProjeDetail, name="proje_detail"),
    path('hakkimizda/', views.AboutView, name='about'),
    path('iletisim/', views.ContactView, name='contact'),
    path('vizyon-misyon/', views.VizyonView, name='vizyon'),
    path('kategori/<slug:slug>/', views.marka_by_category, name='category'),
]
