from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from env import api_key
import requests
import json
from urllib.request import urlopen

api_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + api_key

testing = True

@login_required
def home(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # deal with test case
    if (testing):
        return HttpResponse("Your IP address is : 0.0.0.0 You are visiting from latitude: 12.1234, longitude: -1.1234")
    else:
        print("Here")
        location_json = get_location_data(ip)
        location_data = json.loads(location_json)
        print(location_data)
        country = location_data['country']
        region = location_data['region']
        longitude = location_data['longitude']
        latitude = location_data['latitude']
        str = "Your IP address is : {} \n You are visiting from \
                                latitude: {}, longitude: {}".format(ip, latitude, longitude)
        return HttpResponse(str)


# This is not the user's location but rather the location of the place sending the info
# Due to running on local machine
@login_required
def get_location_data(ip, test):
    # uncomment for current location
    response = requests.get(api_url)  # + "&ip_address=" + ip_address)
    return response.content
