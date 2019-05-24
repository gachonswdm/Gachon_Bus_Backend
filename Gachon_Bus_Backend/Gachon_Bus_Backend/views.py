from django.http import HttpResponse
from django.shortcuts import render
from math import radians, cos, sin, asin, sqrt


def index(request):
    if request.method == 'POST':
        lat1 = float(request.POST.get('lat1'))
        lon1 = float(request.POST.get('lon1'))
        lat2 = float(request.POST.get('lat2'))
        lon2 = float(request.POST.get('lon2'))
        dist = havesine(lat1, lon1, lat2, lon2)
        return render(request, 'templates/index.html', {'dist':dist})
    else:
        return render(request, 'templates/index.html', {})

def havesine(lat1, lon1, lat2, lon2):
    '''
        https://en.wikipedia.org/wiki/Haversine_formula
        Haversine Formula 를 이용해 위도/경도가 주어졌을 때, 구 형태에서의 두 점사이의 거리를 구한다. 
    '''
    '''# convert decimal degrees to radians'''
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # https://en.wikipedia.org/wiki/Haversine_formula
    dlat = lat1 - lat2
    dlon = lon1 - lon2
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # convert to KM
    km = 6367 * c
    return km

'''
In AndroidAPP
double latitude; // static 클래스 변수 위도
double longitube; // static 클래스 변수 경도

'''