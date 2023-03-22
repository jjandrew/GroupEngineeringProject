from submission.models import RoomModel, ImageSubmission, building_choices
from datetime import datetime
from leaderboard.models import BuildingModel


def get_building_name(top_sub):
    # Translate Constant building name to formatted string
    building_name = None
    for choice in building_choices:
        if choice[0] == top_sub.building:
            building_name = choice[1]
            break
    if building_name == None:
        # TODO remove this
        print("Collosal error")
    return building_name


def input_stats(submission: ImageSubmission):
    """Inputs the stats for an image submission into """
    # Check if a room exists
    room = None
    if RoomModel.objects.filter(building=submission.building, name=submission.room.lower()).exists():
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
        building.f_name = get_building_name(submission.building)
        building.save()

    add_stats(submission, room)


def add_stats(submission: ImageSubmission, room: RoomModel):
    """Add the stats from submission to room model"""
    if submission.lights_status == "ON":
        room.number_lights_on += 1
    if submission.windows_status == "OPEN":
        room.number_windows_open += 1
    room.litter_items += submission.litter_items
    room.number_submissions += 1
    room.last_done = datetime.now()
    room.save()
