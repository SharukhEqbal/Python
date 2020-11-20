
# Generator basic program
def create_cubes(n):
    for num in range(n):
        yield num**3

print(create_cubes(5))
for number in create_cubes(5):
    print(number)

"""
o/p:

<generator object create_cubes at 0x00000117766377C8>
0
1
8
27
64


def create_cubes(n):
    result = []
    for num in range(n):
        result.append(num**3)
    return result
print(create_cubes(5)) # [0, 1, 8, 27, 64]
for i in create_cubes(5):
    print(i)

o/p:

[0, 1, 8, 27, 64]
0
1
8
27
64

both returns the result but with generators helps in memory saving
as it will return value one by one from a generator obj

"""
