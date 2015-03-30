
from irondragon import state
from irondragon.framework.api import command
from irondragon.state import expects_game


@command('create-game', verb='post')
def create_game(request):
    id = request['game_id']
    state.initialize_game(id)
    return {
        'response': 'create-game-response',
        'status': 'ok',
    }


@command('join-game', verb='post')
@expects_game
def join_game(request, game):
    # TODO
    return {
        'response': 'join-game-response',
        'status': 'unimplemented',
    }
