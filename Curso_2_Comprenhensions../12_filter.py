numbers = [1, 2, 3, 4]

print(list(filter(lambda x: x%2 == 0, numbers)))

items = [
    {
    'product': 'camisa',
    'price': 100
    },
    {
    'product': 'pantalon',
    'price': 200
    },
    {
    'product': 'zapatos',
    'price': 300
    }
    ]

new_items = list(filter(lambda x: x['price'] > 150, items))

print(f'items: {items}')

print(f'new_items: {new_items}')