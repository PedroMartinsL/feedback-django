from django.views.generic.edit import CreateView
from django.views.generic import ListView

from.models import UserProfile

class CreateProfileView(CreateView):
    template_name = 'profiles/profile.html'
    model = UserProfile
    fields = "__all__"
    success_url = '/profiles' # URL to redirect to after successful form submission

class ProfilesView(ListView):
    model = UserProfile
    template_name = 'profiles/user_profile.html'
    context_object_name = 'profiles' # name exposed to template - list of profiles
    