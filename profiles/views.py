from django.shortcuts import render
from profiles.models import Profile
import logging


logger = logging.getLogger(__name__)


def index(request):
    """
    Display the list of all profiles
    :param request: None
    :return: render and display template as HTML
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Display the detail of a give profile
    :param request: None
    :return: render and display template as HTML
    """
    try:
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except:
        logger.error(f"Username : {username} doesn't exist")
        index(request)
