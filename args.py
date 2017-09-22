
# *args, **kwargs
#refer python 3.0 doc

def cheeseshop(kind, *args, **kwargs):
    print("The word for kind is: ", kind, "!")
    print("The word for args is : ", args)

    print("*" * 50)

    print("The key value pair kwargs is : ", kwargs)

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
