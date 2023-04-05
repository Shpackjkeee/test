X = 99
def f1():
    X = 88
    def f2():
        nonlocal X
        X = 100
        print(X)
    f2()
    print(X)
f1()