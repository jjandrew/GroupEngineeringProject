""" Crowd sources the data for the rooms. """
from datetime import datetime
from leaderboard.models import BuildingModel
from submission.models import RoomModel, ImageSubmission


def input_stats(submission: ImageSubmission) -> None:
    """ Inputs the stats for an image submission into

    Args:
        submission (ImageSubmission): The image submission object to have
            data added to it.
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
        building.save()

    add_stats(submission, room)


def add_stats(submission: ImageSubmission, room: RoomModel) -> None:
    """ Add the stats from submission to room model

    Args:
        submission (ImageSubmission): The image submission object to have
            data added to it.
        room (RoomModel): The room model object to have data added to it.
    """
    if submission.lights_status == "ON":
        room.number_lights_on += 1
    if submission.windows_status == "OPEN":
        room.number_windows_open += 1
    room.litter_items += submission.litter_items
    room.number_submissions += 1
    room.last_done = datetime.now()
    room.save()
