from django.utils import timezone
from shwe_app.models import VisitorCount
from django.conf import settings


class VisitorCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not self.is_development_request(request):
            self.update_visitor_count()

        response = self.get_response(request)
        return response

    def is_development_request(self, request):
        # Add logic to identify your development IP address or any other identifier
        # For example, you might check if the request comes from a specific IP range.
        # Update this based on your actual development environment.
        return (
            hasattr(settings, 'DEVELOPMENT_IP') and
            request.META.get('REMOTE_ADDR') == settings.DEVELOPMENT_IP
        )

    def update_visitor_count(self, request):
        if request.session.get('visited') is None:
            visitor_count, created = VisitorCount.objects.get_or_create(
                date=timezone.now().date())
            visitor_count.count += 1
            visitor_count.save()
            request.session['visited'] = True
