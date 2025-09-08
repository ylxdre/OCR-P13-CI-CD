from django.shortcuts import render


def index(request):
    """
    Main index of app, home page
    :param request: None
    :return: render and display homepage
    """
    return render(request, 'index.html')
