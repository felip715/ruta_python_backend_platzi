#De esta forma agregamos texto al archivo
with open('./text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('\nNueva linea\n')
    file.write('Otra linea mas\n')

#Si utilizamos los permisos w+ lo sobreescribimos
with open('./text.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write('Nueva linea\n')
    file.write('Otra linea mas\n')