# Iteration Multiply 
def mult_iter(a,b):
    result = 0
    while b > 0:
        result += a
        b -=1
    return result

# Recursive Multiply
def mult(a,b):
    if b == 1:
        return a
    else:
        return a+mult(a,b-1)

# Recursive Factorial
def factorial(n):
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)

def fib(x):
    """assumes x an int >=0 returns Fibonacci of x"""
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)


# print(mult_iter(9999, 10))
# print(mult(9999, 10))
# print(factorial(70))
# print('fib 30:',fib(30))

# Dictionaries = {}

my_dict = {'Ana':'B', 'John':'A+', 'Denise':'A'}