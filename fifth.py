def quotient_and_remainder(x,y):
    quotient = x // y
    remainder = x % y
    return (quotient, remainder)

(quot, rem) = quotient_and_remainder(4,5)

print((quot, rem))

# Tuples = () immutable
# Lists = [] mutable

# Clone a List:

satan = ['666',7,'bah']
hell = satan[:] #hell is a cloned list of satan | satan[0:len(satan)]