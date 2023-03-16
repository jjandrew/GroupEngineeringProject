from submission.models import RoomModel, ImageSubmission


def get_statistics(room_name, building):
    """Gets statistics if a room already has statistics entered"""
    rooms = RoomModel.objects.filter(building=building, name=room_name)
    if (len(rooms) == 0):
        print("No room")
        return None
    room = rooms[0]
    number_of_lights = room.number_of_lights
    number_of_windows = room.number_of_windows
    number_plugs = room.number_plugs
    number_submissions = room.number_submissions
    return {
        'lights': number_of_lights,
        'windows': number_of_windows,
        'plugs': number_plugs,
        'submissions': number_submissions
    }


def statistics_valid(submission: ImageSubmission, repeat: bool):
    """Checks if the stats entered in submission are the same a previous submissions"""
    # Get the statistcs from
    stats = get_statistics(submission.room.lower(), submission.building)
    # If there are no stats entered considered valid
    if stats == None:
        return "valid"
    # If all of the stats entered are same then valid
    if submission.number_of_lights == stats['lights'] and submission.number_of_windows == stats['windows'] and submission.number_plugs == stats['plugs']:
        return "valid"
    else:
        # If there have already been 3 or more submissions then invalid
        if stats['submissions'] > 2:
            return "invalid"
        # Ask user to reckeck and then if still different change
        if repeat:
            # Change stats for room
            # Submissions - 1
            return "valid_repeat"
        # If not repeated ask user to recheck
        return "check"


def input_stats(submission: ImageSubmission, repeat: bool):
    # checks if stats valid for room
    stat_check = statistics_valid(submission=submission, repeat=repeat)
    # If they are valid adds the stats
    if stat_check == "valid":
        room
        if RoomModel.objects.filter(building=submission.building, name=submission.room.lower()).exists():
            room = RoomModel.objects.get(
                name=submission.room, building=submission.building)
        else:
            room = RoomModel(name=submission.room,
                             building=submission.building)
        add_stats(submission, room)
        return "complete"
    # If not repeated ask user to recheck or will tell them they are invalid
    if not repeat:
        if stat_check == "check":
            return "check"
        else:
            return "invalid"
    # If a valid repeat then change stats otherwise invalid
    else:
        if stat_check == "valid_repeat":
            room = RoomModel.objects.get(
                name=submission.room, building=submission.building)
            reset_stats(submission, room)
            return "complete"
        else:
            return "invalid"


def add_stats(submission: ImageSubmission, room: RoomModel):
    """Add the stats from submission to room model"""
    room.number_lights_on += submission.number_lights_on
    room.number_windows_open += submission.number_windows_open
    room.number_plugs_on += submission.number_plugs_on
    room.litter_items += submission.litter_items
    room.number_submissions += 1
    room.save()


def reset_stats(submission: ImageSubmission, room: RoomModel):
    """Reset the stats for the room"""
    room.number_of_lights = submission.number_of_lights
    room.number_lights_on = submission.number_lights_on
    room.number_of_windows = submission.number_of_windows
    room.number_windows_open = submission.number_windows_open
    room.number_plugs = submission.number_plugs
    room.number_plugs_on = submission.number_plugs_on
    room.litter_items = submission.litter_items
    room.number_submissions = 1
    room.save()
