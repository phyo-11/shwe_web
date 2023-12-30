from . import views
from django.urls import path

urlpatterns = [
    path('checkout/<int:image_id>/', views.checkout, name='checkout'),
    path('payment-success/<int:image_id>/',
         views.payment_success, name='payment-success'),
    path('payment-failed/<int:image_id>/',
         views.payment_failed, name='payment-failed'),
]
