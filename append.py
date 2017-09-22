
#Append

"""
def f(a, l = None):
    if l is None:
        l = []
    l.append(a)
    return l

print(f(1))
print(f(2)) """

def f(a, l = []):
    l.append(a)
    return l

print(f(1))
print(f(2))
