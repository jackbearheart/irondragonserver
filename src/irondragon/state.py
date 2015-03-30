
from irondragon import static_state

GAMES = {}


def get_game(id):
    return GAMES[id]


def initialize_game(id):
    game = {
        'public': {
            'phase': {
                'game': 'GAME_START',
                'game_special': None,
                'turn': 0,
                'current_player': {
                    'id': None,
                    'turn_phase': None,
                    'money_spent': 0,
                    'moved': 0,
                },
                'history': [],
                'winner': None,
            },
            'effects': {
                'rainbow_bridge': [False, -1],
                'magical_link': [True, -1],
                'no_build': [False, -1],
                'no_move': [False, -1],
                'half_move': [False, -1],  # i.e. [False, -1, 'Northern Wastes']
                'no_load_exchange': [False, -1],
                'no_upgrade': [False, -1],
                'no_ship_change': [False, -1],
                'no_foreman_change': [False, -1],
            },
            'deck': {
                'resources': static_state.load_starting_resources(),
                'foremen': {
                    'discard': [],
                },
                'ships': {
                    'discard': [],
                },
                'demand_event': {
                    'discard': [],
                },
                'trains': static_state.load_trains(),
            },
            'players': {},
            'track': {},
        },
        'private': {
            'deck': {
                'foremen': {
                    'deck': static_state.load_foremen_deck(),
                },
                'ships': {
                    'deck': static_state.load_ships_deck(),
                },
                'demand_event': {
                    'deck': static_state.load_demand_event_deck(),
                },
            },
        },
    }

    global GAMES
    GAMES[id] = game
    return game


def add_player(game, name, color):
    player = {
        'id': name,
        'demands': [],
        'train': None,
        'ship': None,
        'foreman': None,
        'resources': [],
        'gp': 0,
        'color': color,
        'effects': {
            'skip': [False, -1],
            'no_build': [False, -1],
        }
    }
    players = game['public']['players']
    players[player['id']] = player


def shuffle_deck(game, deck_name, discard_pile=False):
    """ Shuffles the deck, possibly together with the discard pile. """
    # TODO
    pass


# a decorator function for an api command that passes in the
# associated game
def expects_game(fxn):
    def decorated_fxn(data, *args, **kwargs):
        game = get_game(data['game_id'])
        return fxn(data, game=game, *args, **kwargs)
    return decorated_fxn
