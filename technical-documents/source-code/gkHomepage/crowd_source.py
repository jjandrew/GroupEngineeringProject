""" Defines how data for the CO2 collection will be crowdsourced. """
from datetime import datetime
from submission.models import RoomModel, ImageSubmission, building_choices
from leaderboard.models import BuildingModel


def get_building_name(top_sub) -> str:
    """ Gets the name of the building.

    Args:
        top_sub: The top building submission, which is having it's
            name collected.

    Returns:
        str: building_name: The name of the building as a string for ease of
            processing.
    """
    # Translate Constant building name to formatted string
    building_name = None
    print(top_sub.building)
    for choice in building_choices:
        if choice[0] == top_sub.building:
            building_name = choice[1]
            break
    if building_name == None:
        print("Collosal error")
    return building_name


def input_stats(submission: ImageSubmission) -> None:
    """ Inputs the stats for an image submission into.

    Args:
        submission: (ImageSubmission): The ImageSubmission model which is
            having it's input stats added to it.
    """
    # Check if a room exists
    room = None
    if RoomModel.objects.filter(building=submission.building,
                                name=submission.room.lower()).exists():
        room = RoomModel.objects.get(
            name=submission.room.lower(), building=submission.building)
    else:
        room = RoomModel(name=submission.room.lower(),
                         building=submission.building)
        room.save()

    # Check if building exists and if not create a new building object
    building = None
    if not BuildingModel.objects.filter(name=submission.building).exists():
        building = BuildingModel(name=submission.building)
        building.f_name = get_building_name(submission)
        building.save()

    add_stats(submission, room)


def add_stats(submission: ImageSubmission, room: RoomModel) -> None:
    """ Add the stats from submission to room model.

    Args:
        submission: (ImageSubmission): The ImageSubmission object representing
            the submission from which the stats are being extracted.
        room: (RoomModel): The Room Model object of the room which is having
            stats added to it.
    """
    if submission.lights_status == "ON":
        room.number_lights_on += 1
    if submission.windows_status == "OPEN":
        room.number_windows_open += 1
    room.litter_items += submission.litter_items
    room.number_submissions += 1
    room.save()
