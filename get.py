
from api import command
import state
from state import expects_game


@command('get')
@expects_game
def get(request, game):
    return game['public']


@command('dump')
def all_state(request):
    """ A debugging command that returns all state. """
    return state.GAMES


@command('resources')
@expects_game
def resources(request, game):
    return game['public']['deck']['resources']
