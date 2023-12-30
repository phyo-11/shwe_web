from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('gallery/', views.gallery, name="gallery"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('standard/<str:type>/', views.standard, name="standard"),
    path('standard/<str:type>/<str:orientation>/',
         views.standard_with_params, name='standard_with_params'),
    path('special/<str:type>/', views.special, name="special"),
    path('special/<str:type>/<str:orientation>/',
         views.special_with_params, name='special_with_params'),
    path('custom/<str:type>/', views.custom, name="custom"),
    path('custom/<str:type>/<str:orientation>/',
         views.custom_with_params, name='custom_with_params'),
]
