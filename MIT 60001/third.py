### APPROXIMATE SOLUTION - CUBE ROOT

cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess,'is close to the cube root of', cube)


### BISECTION SEARCH - CUBE ROOT (FOR CUBE >= 1)
cube = 27
epsilon = 0.01
guess = 0.0
num_guesses = 0
high = cube
low = 0
guess = (high+0)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
        print('low:',low)
    else:
        high = guess
        print('high:',high)
    guess = (high+low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print (guess,'is close to the cube root of', cube)