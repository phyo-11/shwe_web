from django.db import models


class Image(models.Model):
    image_code = models.CharField(max_length=50, unique=True)
    image_width = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    image_height = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    image_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    image_weight = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    image_type = models.CharField(max_length=255, null=True)
    image_orientation = models.CharField(max_length=255, null=True)
    image_description = models.TextField(blank=True)
    image_path = models.CharField(max_length=255)
    image_uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_code



