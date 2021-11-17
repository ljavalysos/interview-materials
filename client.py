"""
BACKGROUND:

You are given an endpoint that returns an ordered list of items, with a maximum of
100 items per page.

http://some-api.com/items

[
    'item_1',
    'item_2',
    ...
]

If there are more than 100 items in total, it will just return the first 100.

In order to get the rest of the items, you'll need to use the `start_key` query
parameter. The start key should be the value of an existing item. If used, the
first item in the response will be start_key, and the rest will be the following
99 items.

If start_key = 'item_n':

[
    'item_n',
    'item_n+1',
    ...
]

There is a fixed order of items. Items are always returned in the same order.


PROBLEM:

Using an object-oriented approach, modify the API client class to gather all items
from the /items endpoint.

Hint: you don't know how many items there are in total.
"""

import requests


class APIClient:

    HOST_URL = 'http://127.0.0.1:5000'

    @classmethod
    def make_request(cls, start_key=None):
        """Makes request to items endpoint. Returns a list of strings.

        :rtype: [str]
        """
        url = f'{cls.HOST_URL}/items'

        if start_key:
            url = f'{url}?start_key={start_key}'

        response = requests.get(url)

        return response.json()


if __name__ == '__main__':
    pass
