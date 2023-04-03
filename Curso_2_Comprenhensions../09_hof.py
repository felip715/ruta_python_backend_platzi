def increment(x):
    return x + 1

increment_v2 = lambda x: x+1

def hof(x, func):
    return x + func(x)

print(hof(2, increment))

print(hof(2, increment_v2))