from leaderboard.annual_building_usage import building_usage
from leaderboard.models import BuildingModel
from submission.models import ImageSubmission
from math import log10, floor


def round_5(x, sig=5):
    """Round a float to five significant figures"""
    return round(x, sig-int(floor(log10(abs(x))))-1)


def get_co2(sub: ImageSubmission, building_name: str):
    """Gets the co2 emmissions for widows open and lights on"""
    # Get the building and the lights and window status
    building = BuildingModel.objects.get(name=building_name)
    windows = sub.windows_status
    lights = sub.lights_status

    # Get assumed energy usage per 6 hours
    # Get the number of rooms in building by energy usage by building as a percentage of total usage
    # Assumes you are saving for a whole 6 hours
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
