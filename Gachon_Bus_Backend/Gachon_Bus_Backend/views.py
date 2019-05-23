from django.http import HttpResponse


def index(request):
    return HttpResponse("This is Django For Gachon_Bus_Backend!")