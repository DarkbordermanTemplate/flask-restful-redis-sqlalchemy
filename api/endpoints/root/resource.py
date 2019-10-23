from flask_restful import Resource


class RootResource(Resource):
    def __init__(self):
        self._set_get_parser()

    def _set_get_parser(self):
        pass

    # pylint: disable=R0201
    def get(self):
        return 'hello world', 200
