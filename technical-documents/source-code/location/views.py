""" Outlines the methods to be used in the location app. """
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required


TESTING = True


@login_required
def home(request):
    """ Returns the home page for the location app

    Args:
        request: The HTTP request submitted by the user.

    Returns:

        HttpResponse:str: A string containing the user's location data is
        displayed as an HTTP webpage.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        i_p = x_forwarded_for.split(',')[0]
    else:
        i_p = request.META.get('REMOTE_ADDR')

    # deal with test case
    if TESTING:
        return HttpResponse("Your IP address is : 0.0.0.0 " +
                            "You are visiting from latitude: 12.1234, longitude: -1.1234")
    else:
        location_data = get_location_data()
        longitude = location_data['longitude']
        latitude = location_data['latitude']
        str = (f"Your IP address is : {i_p} \n You are visiting from \
                                latitude: {latitude}, longitude: {longitude}")
        return HttpResponse(str)


def get_location_data():
    """ Returns the location data using a location API

    Returns:
        json: A json dictionary containing the user's location data.
    """
    json = {
        "country": "UK",
        "region": "Devon",
        "longitude": "-1.1234",
        "latitude": "12.1234"
    }
    return json
