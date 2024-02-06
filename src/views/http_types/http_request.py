from typing import Dict

class HttpRequest:
    def __init__(self, query_params: Dict = None, headers: Dict = None, body: Dict = None):
        self.query_params = query_params
        self.headers = headers
        self.body = body
