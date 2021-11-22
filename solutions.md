# Solutions

## Client

They should add a method to API client class:

```python

class APIClient:

	...etc...

    def get_items(self):
        items = []
        response = self.make_request()
        items.extend(response)

        while len(response) == 100:
            start_key = response[-1]
            response = self.make_request(start_key)
            items.append(response[0:99])

        return items
```

and then call it:

```python
if __name__ == '__main__':
	client = APIClient()
    items = client.get_items()
    print(f'Got {len(items)} items!')
```


## Server

```python
def get_items():
    """Returns a list of 100 items, beginning with the start key."""
    start_key = request.args.get('start_key')
    
    if start_key:
        start_item = Item.query.filter(Item.name == start_key).one().id
        entries = Item.query.offset(start_item.id - 1).limit(100).all()
    else:
        entries = Item.query.offset(0).limit(100).all()

    out = []
    for entry in entries:
        out.append(entry.name)
    return jsonify(out)
```