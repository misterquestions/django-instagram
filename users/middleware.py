from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """Ensures the user completes its profile first to be able to use the platform"""

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous and not request.user.is_staff:
            profile = request.user.profile

            print(f'profile is {profile}')

            if not profile.profile_picture or not profile.biography:
                if request.path not in [reverse('update_profile'), reverse('logout')]:
                    return redirect('update_profile')

        response = self.get_response(request)
        return response