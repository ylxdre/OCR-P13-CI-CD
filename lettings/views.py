from django.shortcuts import render
from lettings.models import Letting


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
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
