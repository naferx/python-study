'''
my_list = ['Mary', 'had', 'a', 'little', 'lamb']

def my_list(my_list):
    del my_list[3]
    my_list = 'ram'

print(my_list(my_list))
'''

'''
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return

print(fun(fun(2)) + 1)
'''

'''
tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)
'''

'''
def fun(x):
    global y
    y = x * x
    return y

fun(2)
print(y)
'''

'''
tup = (3, 4, 5)

tup[0] = tup[1] + tup[2]



def func(a, b):
    return a ** a

print(func(2))



def func(inp=2, out=3):
    return inp * out

print(func(out=2))

'''


dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )
    print(dictionary)

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    print(k[0])


def fn():
    ...


print(fn())