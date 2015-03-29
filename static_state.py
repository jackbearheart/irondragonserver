

GEOGRAPHY = {}


def load_static_geography():
    global GEOGRAPHY
    GEOGRAPHY = {
        'mileposts': [],
        'special_links': {},
        'rivers': {},
        'city_to_resource': {},
    }


def get_geography():
    return GEOGRAPHY


def load_starting_resources():
    return {
        'ale': 4,
        'armor': 4,
        # TODO
        'wine': 4,
    }


def load_trains():
    # TODO
    return {}


def load_foremen_deck():
    # TODO
    return []


def load_ships_deck():
    # TODO
    return []


def load_demand_event_deck():
    # TODO
    return []
