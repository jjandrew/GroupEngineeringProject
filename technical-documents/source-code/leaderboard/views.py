""" Outlines the functions to be used by the leaderboard. """
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from submission.models import building_choices
from leaderboard.models import BuildingModel
from leaderboard.co2_calcs import round_5


def get_building_name(const: str) -> str:
    """ If the building name is valid, it is returned to the user.

    Args:
        const: (str): The name of the building as a string for ease of
            processing.

    Returns:
        str: building_name: The name of the building as a string for ease
            of processing.
    """
    # Translate Constant building name to formatted string
    building_name = None
    for choice in building_choices:
        if choice[0] == const:
            building_name = choice[1]
            break
    if building_name == None:
        print("Collosal error")
    return building_name


@login_required
def leaderboard(request):
    """ A function for displaying and ordering (in descending order) the
    leaderboard. Note, to access this, the user must be logged in.

    Args:
        request: The HTTP request submitted by the user.

    Returns:
        render(): For either the building or player leaderboard, depending on
            the number of users or buildings, a different version of the
            leaderboard is presented to the user (i.e. If there is one
            building, or only two players).
    """

    to_use = 'players'

    players = CustomUser.objects.filter(points__gt=0).order_by('-points')
    buildings = BuildingModel.objects.filter(co2__gt=0).order_by('co2')

    # Exception checking for the player leaderboard
    if to_use == 'players':
        try:
            first = players[0]
            second = players[1]
            third = players[2]
            remaining = players[3:]

            return render(request,
                          'UI/player_leaderboard.html',
                          {'first': first,
                           'second': second,
                           'third': third,
                           'remaining': remaining})
        except IndexError:
            try:
                return render(request,
                              'UI/player_leaderboard.html',
                              {'first': first,
                               'second': second,
                               'third': third,
                               'remaining': []})
            except UnboundLocalError:
                try:
                    third = {
                        'username': "Insufficient Users",
                        'points': 0
                    }
                    return render(request,
                                  'UI/player_leaderboard.html',
                                  {'first': first,
                                   'second': second,
                                   'third': third,
                                   'remaining': []})
                except UnboundLocalError:
                    try:
                        second = {
                            'username': "Insufficient Users",
                            'points': 0
                        }
                        return render(request,
                                      'UI/player_leaderboard.html',
                                      {'first': first,
                                       'second': second,
                                       'third': third,
                                       'remaining': []})
                    except UnboundLocalError:
                        first = {
                            'username': "Insufficient Users",
                            'points': 0
                        }
                        return render(request,
                                      'UI/player_leaderboard.html',
                                      {'first': first,
                                       'second': second,
                                       'third': third,
                                       'remaining': []})
    else:
        # Goes through the same exception checking but for the building
        # leaderboard
        for building in buildings:
            building.norm_co2 = round_5(
                building.co2 / building.number_submissions)
        try:
            first = buildings[0]
            first_name = get_building_name(first.name)
            second = buildings[1]
            second_name = get_building_name(second.name)
            third = buildings[2]
            third_name = get_building_name(third.name)
            remaining = buildings[3:]
            remaining_names = []
            for building in remaining:
                building.f_name = get_building_name(building.name)
                building.save()

            return render(request,
                          'UI/building_leaderboard.html',
                          {'first': first,
                           'second': second,
                           'third': third,
                           'remaining': remaining,
                           'first_name': first_name,
                           'second_name': second_name,
                           'third_name': third_name,
                           'remaining_names': remaining_names, })
        except IndexError:
            try:
                return render(request,
                              'UI/building_leaderboard.html',
                              {'first': first,
                               'second': second,
                               'third': third,
                               'remaining': [],
                               'first_name': first_name,
                               'second_name': second_name,
                               'third_name': third_name,
                               'remaining_names': []})
            except UnboundLocalError:
                try:
                    third = {
                        'norm_co2': 0
                    }
                    third_name = "No buildings"
                    return render(request,
                                  'UI/building_leaderboard.html',
                                  {'first': first,
                                   'second': second,
                                   'third': third,
                                   'remaining': [],
                                   'first_name': first_name,
                                   'second_name': second_name,
                                   'third_name': third_name,
                                   'remaining_names': []})
                except UnboundLocalError:
                    try:
                        second = {
                            'norm_co2': 0
                        }
                        second_name = "No buildings"
                        return render(request,
                                      'UI/building_leaderboard.html',
                                      {'first': first,
                                       'second': second,
                                       'third': third,
                                       'remaining': [],
                                       'first_name': first_name,
                                       'second_name': second_name,
                                       'third_name': third_name,
                                       'remaining_names': []})
                    except UnboundLocalError:
                        first = {
                            'norm_co2': 0
                        }
                        first_name = "No buildings"
                        return render(request,
                                      'UI/building_leaderboard.html',
                                      {'first': first,
                                       'second': second,
                                       'third': third,
                                       'remaining': [],
                                       'first_name': first_name,
                                       'second_name': second_name,
                                       'third_name': third_name,
                                       'remaining_names': []})
