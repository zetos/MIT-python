# A function that search for an element in a list
def search_for_element(L, e):
    for i in L:
        if i == e:
            return True
    return False

def linear_search(L, e): # O(n)
    found = False
    for i in range(len(L)):
        if e == L[i]: #O(1)
            found = True
    return found

def sorted_list_search(L, e): #O(n)
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False



lista = [0,666,900]
element = 0

print('Search:', search_for_element(lista,element))
print('Linear Search:', linear_search(lista,element))
print('Sorted List Search:', sorted_list_search(lista,element))
