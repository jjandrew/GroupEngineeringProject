""" Outlines the methods to be used in the leaderboard app. """
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from submission.models import building_choices
from leaderboard.models import BuildingModel


@login_required
def leaderboard(request):
    """ A function for displaying and ordering (in descending order) the
    leaderboard. Note, to access this, the user must be logged in.

    Args:
        request: The HTTP request submitted by the user.

    Returns:
        render: Returns the leaderboard page with different values, depending
        on whether or not certain criteria are met.
    """
    leaderboard = CustomUser.objects.filter(points__gt=0).order_by('-points')

    buildings = BuildingModel.objects.order_by('co2')

    try:
        # Gets the users in 1st, 2nd and 3rd place on the leaderboard
        first = leaderboard[0]
        second = leaderboard[1]
        third = leaderboard[2]
        remaining = leaderboard[3:]

        # Gets the buildings in 1st, 2nd and 3rd place on the leaderboard
        building_names = dict(building_choices)
        building1 = buildings[0]
        building1.name = building_names[building1.name]
        building2 = buildings[1]
        building2.name = building_names[building2.name]
        building3 = buildings[2]
        building3.name = building_names[building3.name]
        rem_building = buildings[3:]

        # Gets the names of the remaining buildings
        for building in rem_building:
            building.name = building_names[building.name]

        return render(request, 'UI/leaderboard2.html',
                      {'first': first,
                       'second': second,
                       'third': third,
                       'remaining': remaining,
                       "building1": building1,
                       "building2": building2,
                       "building3": building3,
                       "buildings": rem_building})
    except IndexError:
        try:
            # Exceptions for if the leaderboard accesses more players than there currently are
            return render(request, 'UI/leaderboard.html',
                          {'first': first, 'second': second, 'third': third, 'remaining': []})
        except UnboundLocalError:
            try:
                # Exceptions for if there are only two players
                third = {
                    'username': "Insufficient Users",
                    'points': 0
                }
                return render(request, 'UI/leaderboard.html',
                              {'first': first, 'second': second, 'third': third, 'remaining': []})
            except UnboundLocalError:
                try:
                    # Exceptions for if there is only one player
                    second = {
                        'username': "Insufficient Users",
                        'points': 0
                    }
                    return render(request, 'UI/leaderboard.html',
                                  {'first': first,
                                   'second': "Insufficient Players",
                                   'third': "Insufficient Players",
                                   'remaining': []})
                except UnboundLocalError:
                    # Exceptions for if there are no players
                    first = {
                        'username': "Insufficient Users",
                        'points': 0
                    }
                    return render(request,
                                  'UI/leaderboard.html',
                                  {'first': "Insufficient Players",
                                   'second': "Insufficient Players",
                                   'third': "Insufficient Players",
                                   'remaining': []})
