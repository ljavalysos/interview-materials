"""Write an API client against your server.

Feel free to reference the following requests docs:
https://docs.python-requests.org/en/latest/user/quickstart/
"""

import requests


class APIClient:

    HOST_URL = 'http://127.0.0.1:5000'

    @classmethod
    def make_request(cls):
        """Makes request to items endpoint. Returns a list of strings.

        :rtype: [str]
        """
        url = f'{cls.HOST_URL}/incidents'
        response = requests.get(url)

        response.raise_for_status()

        return response.json()


if __name__ == '__main__':
    # Fill in
    pass
