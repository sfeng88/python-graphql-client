from six.moves import urllib
import json

class GraphQLClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.token = None
        self.headers = {'Accept': 'application/json',
                        'Content-Type': 'application/json'}

    def execute(self, query, variables=None):
        return self._send(query, variables)

    def inject_token(self, token):
        self.token = token

    def add_header(self, key, value):
        self.headers[key] = '{}'.format(value)

    def _send(self, query, variables):
        data = {'query': query,
                'variables': variables}

        if self.token is not None:
            self.headers['Authorization'] = '{}'.format(self.token)

        print (self.headers)

        req = urllib.request.Request(self.endpoint, json.dumps(data).encode('utf-8'), self.headers)

        try:
            response = urllib.request.urlopen(req)
            return response.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            print((e.read()))
            print('')
            raise e
