from django.shortcuts import render
from shwe_app.models import Image
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse


def checkout(request, image_id):
    image = Image.objects.get(id=image_id)

    host = request.get_host()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': image.image_price,
        'item_name': image.image_code,
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('payment-success', kwargs = {'image_id': image.id})}",
        'cancel_url': f"http://{host}{reverse('payment-failed', kwargs = {'image_id': image.id})}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'image': image,
        'paypal': paypal_payment,
    }

    return render(request, 'checkout.html', context)


def payment_success(request, image_id):
    image = Image.objects.get(id=image_id)

    context = {
        'image': image,
    }

    return render(request, 'payment_success.html', context)


def payment_failed(request, image_id):
    image = Image.objects.get(id=image_id)

    context = {
        'image': image,
    }

    return render(request, 'payment_failed.html', context)
