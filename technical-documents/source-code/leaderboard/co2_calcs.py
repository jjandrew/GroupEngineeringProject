""" Outlines the methods for calculating the CO2 figures for a building. """
from math import log10, floor
from submission.models import ImageSubmission
from leaderboard.annual_building_usage import building_usage
from leaderboard.models import BuildingModel


def round_5(number: float, sig=5) -> float:
    """ Round a float to five significant figures.

    Args:
        x: (float): The float number to be rounded.

        sig: (int): The number of significant figures the provided number
            is to be rounded to.

    Returns:
        float:x: The provided number rounded to the given number of
            significant figures, given as a float for ease of processing.
    """
    return round(number, sig-int(floor(log10(abs(number))))-1)


def get_co2(sub: ImageSubmission, building_name: str) -> float:
    """Gets the co2 emmissions for widows open and lights on.

    Args:
        sub: (ImageSubmission): The submitted image, given as an
            ImageSubmission object.

        building_name: str: The name of the building as a string, for ease
            of processing.

    Returns:
        usage: float: The CO2 usage for the provided building given as a float
            for ease of processing.
    """
    # Get the building and the lights and window status
    building = BuildingModel.objects.get(name=building_name)
    windows = sub.windows_status
    lights = sub.lights_status

    # Get assumed energy usage per day
    # Get the number of rooms in building by energy usage by building as a
    # percentage of total usage
    # Assumes you are saving for a whole day

    rooms_in_building = (building_usage['kwh'][sub.building] /
                         building_usage['total_kwh']) * building_usage['approx_total_rooms']

    co2_p_kwh = building_usage['percentage_non_renewable'] * \
        building_usage['co2_per_kwh']
    building_kwh_p_6hr = building_usage['kwh'][sub.building]/365/4
    room_usage_6hr = (1/rooms_in_building) * building_kwh_p_6hr * co2_p_kwh

    # Get the usage calculated if windows are open or lighting on
    usage = 0
    if windows == "OPEN":
        usage += (building_usage['window_loss'] * room_usage_6hr)
    if lights == "ON":
        usage += (building_usage['lighting_loss'] * room_usage_6hr)
    if usage != 0:
        building.co2 += usage
        building.co2 = round_5(building.co2)

    building.number_submissions += 1
    building.save()

    return usage
