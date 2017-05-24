def quotient_and_remainder(x,y):
    quotient = x // y
    remainder = x % y
    return (quotient, remainder)

(quot, rem) = quotient_and_remainder(4,5)

print((quot, rem))