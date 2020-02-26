a = 100  # Global Variable (At module level or outside of the class. Can be accessed everywhere in the same module.)
print("1---", a)


def f1():
    #print("2---", a)
    # global a  # Use of global keyword (To modify the value of global variable inside function/method)
    a = 200  # Local Variable (Inside the function/method)
    print("3---", a)

    def f2():
        #print("5---", a)
        nonlocal a  # Use of nonlocal keyword (To modify the value of local variable inside inner function)
        a=300  # Local Variable (Inside the function/method)
        print("6---", a)
    print("4---", a)
    f2()
    print("7---", a)


f1()
print("8---", a)




'''
1. In case of nested function local variable of outer function can be accessed inside inner function easily. 
'''



