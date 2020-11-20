# Fibonacci series 1,1,2,3,5,8,... using generators
def get_fibonacci():
    a = 1
    b = 1
    for num in range(5):
        yield a # this will remember the value of a for next iteration
        a,b = b, a + b
[i for i in get_fibonacci()]

"""
o/p:
    [1, 1, 2, 3, 5]


def get_fibonacci_without_generator():
    a = 1
    b = 1
    result = []
    for num in range(5):
        result.append(a)
        a,b = b, a+b
    return result
print(get_fibonacci_without_generator())

"""
