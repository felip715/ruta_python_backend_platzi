try:
    print(0/0)
    assert 1 != 1, 'Uno no es distinto que uno'
    age = 17
    if age < 18:
        raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
# Podemos crear excepciones para nuestros errore
except Exception as error:
    print(error)

print('hola')

# Cuando encuentra un error, sale del try