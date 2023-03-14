from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
import requests
import json
from urllib.request import urlopen

testing = True


@login_required
def home(request):
    """Returns the home page for the location app"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # deal with test case
    if (testing):
        return HttpResponse("Your IP address is : 0.0.0.0 You are visiting from latitude: 12.1234, longitude: -1.1234")
    else:
        location_data = getLocationData()
        country = location_data['country']
        region = location_data['region']
        longitude = location_data['longitude']
        latitude = location_data['latitude']
        str = "Your IP address is : {} \n You are visiting from \
                                latitude: {}, longitude: {}".format(ip, latitude, longitude)
        return HttpResponse(str)


def getLocationData():
    """Returns the location data using a location API"""
    json = {
        "country": "UK",
        "region": "Devon",
        "longitude": "-1.1234",
        "latitude": "12.1234"
    }
    return json
