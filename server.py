from twisted.internet import reactor
from twisted.web import resource
from twisted.web.server import Site
from twisted.web.static import File

import api


class IronDragonServer(resource.Resource):
    def render_GET(self, request):
        return api.get(request)

    def render_POST(self, request):
        return api.post(request)


def main():
    root = File('.')
    root.putChild('api', IronDragonServer())
    reactor.listenTCP(8000, Site(root))
    reactor.run()

if __name__ == '__main__':
    main()
