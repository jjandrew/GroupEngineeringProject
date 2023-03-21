""" Outlines the methods to be used in the leaderboard app. """
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from submission.models import building_choices
from leaderboard.models import BuildingModel


def get_building_name(const):
    # Translate Constant building name to formatted string
    building_name = None
    for choice in building_choices:
        if choice[0] == const:
            building_name = choice[1]
            break
    if building_name == None:
        # TODO remove this
        print("Collosal error")
    return building_name


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

    to_use = 'player'

    players = CustomUser.objects.filter(points__gt=0).order_by('-points')
    buildings = BuildingModel.objects.filter(co2__gt=0).order_by('co2')

    if to_use == 'players':
        try:
            first = players[0]
            second = players[1]
            third = players[2]
            remaining = players[3:]

            return render(request, 'UI/player_leaderboard.html', {'first': first, 'second': second, 'third': third, 'remaining': remaining})
        except IndexError:
            try:
                return render(request, 'UI/player_leaderboard.html', {'first': first, 'second': second, 'third': third, 'remaining': []})
            except UnboundLocalError:
                try:
                    third = {
                        'username': "Insufficient Users",
                        'points': 0
                    }
                    return render(request, 'UI/player_leaderboard.html', {'first': first, 'second': second, 'third': third, 'remaining': []})
                except UnboundLocalError:
                    try:
                        second = {
                            'username': "Insufficient Users",
                            'points': 0
                        }
                        return render(request, 'UI/player_leaderboard.html', {'first': first, 'second': second,
                                                                              'third': third, 'remaining': []})
                    except UnboundLocalError:
                        first = {
                            'username': "Insufficient Users",
                            'points': 0
                        }
                        return render(request, 'UI/player_leaderboard.html', {'first': first, 'second': second,
                                                                              'third': third, 'remaining': []})
    else:
        try:
            first = buildings[0]
            print("accessed")
            first_name = get_building_name(first.name)
            second = buildings[1]
            second_name = get_building_name(second.name)
            third = buildings[2]
            third_name = get_building_name(third.name)
            remaining = buildings[3:]
            remaining_names = []
            for building in remaining:
                remaining_names.append(get_building_name(building.name))

            return render(request, 'UI/building_leaderboard.html', {'first': first, 'second': second, 'third': third, 'remaining': remaining, 'first_name': first_name, 'second_name': second_name, 'third_name': third_name, 'remaining_names': remaining_names, })
        except IndexError:
            try:
                return render(request, 'UI/building_leaderboard.html', {'first': first, 'second': second, 'third': third, 'remaining': [], 'first_name': first_name, 'second_name': second_name, 'third_name': third_name, 'remaining_names': []})
            except UnboundLocalError:
                try:
                    third = {
                        'co2': 0
                    }
                    third_name = "No buildings"
                    return render(request, 'UI/building_leaderboard.html', {'first': first, 'second': second, 'third': third, 'remaining': [], 'first_name': first_name, 'second_name': second_name, 'third_name': third_name, 'remaining_names': []})
                except UnboundLocalError:
                    try:
                        second = {
                            'co2': 0
                        }
                        second_name = "No buildings"
                        return render(request, 'UI/building_leaderboard.html', {'first': first, 'second': second, 'third': third, 'remaining': [], 'first_name': first_name, 'second_name': second_name, 'third_name': third_name, 'remaining_names': []})
                    except UnboundLocalError:
                        first = {
                            'co2': 0
                        }
                        first_name = "No buildings"
                        return render(request, 'UI/building_leaderboard.html', {'first': first, 'second': second, 'third': third, 'remaining': [], 'first_name': first_name, 'second_name': second_name, 'third_name': third_name, 'remaining_names': []})
