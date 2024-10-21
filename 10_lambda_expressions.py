'''
A lambda is a small anonymous function 
It can take any number of arguments, but can only have one expression
'''

print('\nLambda expressions')

# lambda arguments: expression

sum = lambda n: n + 10
print(sum(5))

mult = lambda n, m: n * m
print(mult(5, 8))

# Lambda expressions are used to create anonymous functions. The expression
# 'lambda parameters: expression' yields a function object. The unnamed object behaves like a function
# object defined with:
# def <lambda>(parameters):
#   return expression



print('\nReturning lambdas as functions')

# using lambda inside another function

def times(n: int):
    return lambda x: x * n

doubler = times(2)
tripler = times(3)
print(doubler(5))
print(tripler(5))