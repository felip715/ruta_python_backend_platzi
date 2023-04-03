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
prices = list(map(lambda items: items['price'], items))
print(prices)

#si queremos agregar impuestos a un nuevo diccionario hacemos lo siguiente

def add_taxes(items):
    new_items = items.copy()
    new_items['taxes'] = new_items['price'] * .24
    return new_items

new_items = list(map(add_taxes, items))

print(items)
print(new_items)