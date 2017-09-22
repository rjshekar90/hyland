
#py 3
# arbitrary args lists
"""
def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))
"""
#*************************************
#unpacking args list
"""
args = [3, 6]
print list(range(*args))    """

#**************************************

#lambda fns.
def make_incrementor(n):
    return lambda x: x+n

f = make_incrementor(42)

print(f(3))
