from django.shortcuts import render
from . models import Image
import random


def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', {'images': images})


def gallery(request):
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def standard(request, type):
    images = Image.objects.filter(image_type=type)
    shuffled_images = list(images)
    random.shuffle(shuffled_images)
    return render(request, 'standard.html', {'images': shuffled_images})


def standard_with_params(request, orientation, type):
    images = Image.objects.filter(
        image_orientation=orientation, image_type=type)
    shuffled_images = list(images)
    random.shuffle(shuffled_images)
    return render(request, 'standard_with_params.html', {'images': shuffled_images})


def special(request, type):
    images = Image.objects.filter(image_type=type)
    shuffled_images = list(images)
    random.shuffle(shuffled_images)
    return render(request, 'special.html', {'images': shuffled_images})


def special_with_params(request, orientation, type):
    images = Image.objects.filter(
        image_orientation=orientation, image_type=type)
    shuffled_images = list(images)
    random.shuffle(shuffled_images)
    return render(request, 'special_with_params.html', {'images': shuffled_images})


def custom(request, type):
    images = Image.objects.filter(image_type=type)
    return render(request, 'custom.html', {'images': images})


def custom_with_params(request, orientation, type):
    images = Image.objects.filter(
        image_orientation=orientation, image_type=type)
    return render(request, 'custom_with_params.html', {'images': images})
