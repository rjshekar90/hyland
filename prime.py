

# prime no

def prime(num):
    start = 2
    last = 100
    for num in range(start, last+1):
        if num > 1:

            for i in range(2, num):
                if num%i == 0:
                    break
            else:
                print num


prime(100)
