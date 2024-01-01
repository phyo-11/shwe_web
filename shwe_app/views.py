from django.shortcuts import render
from django.http import HttpResponseServerError
from .models import Image, VisitorCount
from django.utils import timezone
import random

def home(request):
    try:
        # Get or create the VisitorCount object for today
        count_object, created = VisitorCount.objects.get_or_create(date=timezone.now().date())

        # Increment the count
        count_object.count += 1
        count_object.save()

    except Exception as e:
        # Handle other exceptions (e.g., database errors) as needed
        return HttpResponseServerError(f"Error: {e}")

    # Retrieve the updated count
    visitor_count = count_object.count

    # Retrieve all images
    images = Image.objects.all()

    # Render the template with the data
    return render(request, 'home.html', {'images': images, 'visitor_count': visitor_count, 'created': created})




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
