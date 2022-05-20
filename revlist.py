def last(a):
    return a[-1] 
def sort(tuples):
    return sorted(tuples, key=last)
i=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("Sorted:")
print(sort(i))