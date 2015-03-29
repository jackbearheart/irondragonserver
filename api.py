
import json


def get(request):
    data = request.args
    for k in data:
        data[k] = data[k][0]
    command_name = data.get('cmd', 'get')
    cmd = COMMANDS['get'][command_name]
    result = cmd['fxn'](data)
    return json.dumps(result)


def post(request):
    raw_data = request.content.getvalue()
    data = json.loads(raw_data)
    cmd = COMMANDS['post'][data['cmd']]
    result = cmd['fxn'](data)
    return json.dumps(result)


COMMANDS = {
    'get': {},
    'post': {},
}


def command(name, verb='get'):
    def decorator(fxn):
        COMMANDS[name] = {
            'name': name,
            'fxn': fxn,
            'verb': verb,
        }
        return fxn
    return decorator
