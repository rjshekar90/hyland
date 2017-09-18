

def rev(s):

    l = []
    for i in s:
        l.append(str(i))


#def reverse(l):
    start = 0
    end = len(l) - 1
    length = len(l)

    while start < end:
        temp = l[start]
        l[start] = l[end]
        l[end] = temp
        start += 1
        end -= 1
    return "".join(l)

print rev("hello")
