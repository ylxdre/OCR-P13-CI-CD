from django.shortcuts import render
from lettings.models import Letting
import logging


logger = logging.getLogger(__name__)


def index(request):
    """
    letting's index page. Retrieve all objects in db then give list to template
    :param request; None
    :return: render and display template HTML
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    display detail of a particular Letting object
    :param request: None
    :return: render and display template HTML
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        print("that")
        return render(request, 'lettings/letting.html', context)
    except:
        logger.error(f"letting id : {letting_id} not found")
        index(request)
