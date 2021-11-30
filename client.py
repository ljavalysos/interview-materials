"""Write an API client against your server.

Feel free to reference the following requests docs:
https://docs.python-requests.org/en/latest/user/quickstart/
"""

import json
import requests
import sys
import urllib.parse


class APIClient:

    HOST_URL = 'http://127.0.0.1:5000'

    @classmethod
    def make_request(cls, url_path):
        """Makes request to items endpoint. Returns a list of strings.

        :param str url_path: URL path to make GET request to
        :rtype: [str]
        """
        url = urllib.parse.urljoin(cls.HOST_URL, url_path)
        response = requests.get(url)
        response.raise_for_status()

        return response.json()


if __name__ == '__main__':
    try:
        url_path = sys.argv[1]
    except IndexError:
        url_path = '/incidents'

    client = APIClient()
    resp = client.make_request(url_path)
    print(json.dumps(resp, indent=2))
