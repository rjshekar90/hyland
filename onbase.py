

# Onbase pgm

def onbase(lst):
    for i in range(1, lst+1):
        if i%3 == 0 and i%7 == 0:
            print "OnBase"
        elif i%3 == 0:
            print "On"
        elif i%7 == 0:
            print "Base"
        else:
            print i

onbase(100)
