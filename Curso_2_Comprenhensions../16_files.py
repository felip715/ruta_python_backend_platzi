#file = open('./text.txt')
#print(file.read())

#print(file.readlines())    Con esto transforma en un vector con las lineas como elementos

"""
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())"""


#file.close()

with open('./text.txt') as file:
    for line in file:
        print(line)
