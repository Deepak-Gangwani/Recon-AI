# internet_middleware.py

import requests
from django.shortcuts import redirect
from django.urls import reverse

class InternetCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check internet connectivity
        try:
            requests.get("http://www.google.com", timeout=5)  # or any other reliable endpoint
            request.session.pop('internet_failure', None)  # Remove the session variable if internet is back
        except requests.ConnectionError:
            # Redirect to the failure page if there's no internet connection and if not already redirected
            if not request.session.get('internet_failure'):
                request.session['internet_failure'] = True
                return redirect(reverse('internet_failure'))

        response = self.get_response(request)

        return response
