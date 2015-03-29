
GAMES = {}


def get_game(id):
    return GAMES[id]


def initialize_game(id):
    game = {
        'public': {
        },
        'private': {},
    }

    GAMES[id] = game
    return game


# a decorator function for an api command that passes in the
# associated game
def expects_game(fxn):
    def decorated_fxn(data, *args, **kwargs):
        game = get_game(data['game_id'])
        return fxn(data, game=game, *args, **kwargs)
    return decorated_fxn
