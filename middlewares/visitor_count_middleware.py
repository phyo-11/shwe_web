from django.utils import timezone
from shwe_app.models import VisitorCount
from django.conf import settings

class VisitorCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not self.is_development_request(request):
            self.update_visitor_count(request)

        response = self.get_response(request)
        return response

    def is_development_request(self, request):
        return (
            hasattr(settings, 'DEVELOPMENT_IP') and
            request.META.get('REMOTE_ADDR') == settings.DEVELOPMENT_IP
        )

    def update_visitor_count(self, request):
        if request.session.get('visited') is None:
            try:
                # Get or create the VisitorCount object for today
                visitor_count, created = VisitorCount.objects.get_or_create(date=timezone.now().date())

                # Increment the count
                visitor_count.count += 1
                visitor_count.save()
                request.session['visited'] = True

            except Exception as e:
                # Handle exceptions (e.g., database errors) as needed
                print(f"Error updating visitor count: {e}")
