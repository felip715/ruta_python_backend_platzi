import csv

def read_csv(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        # obtenemos las cabeceras
        header = next(reader)
        data = []
        for row in reader:
            # creamos tuplas con cabecera y datos
            iterable = zip(header, row)
            # creamos un diccionario y lo añadimos a una lista
            product_dict = {key: value for key, value in iterable}
            data.append(product_dict)
    return data

if __name__ == '__main__':
    data = read_csv('./productos.csv')
    print(data)