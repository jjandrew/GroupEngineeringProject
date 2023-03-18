from submission.models import RoomModel, ImageSubmission


def input_stats(submission: ImageSubmission):

    room = None
    if RoomModel.objects.filter(building=submission.building, name=submission.room.lower()).exists():
        room = RoomModel.objects.get(
            name=submission.room, building=submission.building)
    else:
        room = RoomModel(name=submission.room,
                         building=submission.building)
        room.save()
    add_stats(submission, room)


def add_stats(submission: ImageSubmission, room: RoomModel):
    """Add the stats from submission to room model"""
    if submission.lights_status == "ON":
        room.number_lights_on += 1
    if submission.windows_status == "OPEN":
        room.number_windows_open += 1
    room.litter_items += submission.litter_items
    room.number_submissions += 1
    room.save()
