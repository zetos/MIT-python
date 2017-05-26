# Exceptions

def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] """

    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = not a number
        except:
            raise ValueError('get_ratios called with a bad arg')
    return ratios


def avg(grades):
    assert not len(grades) == 0, 'no grades data'
    return sum(grades)/len(grades)

resultOne = get_ratios([5,6,4],[5,6,1])
resultTwo = avg([6,6,6])

print('result one:',resultOne)
print('result two:',resultTwo)