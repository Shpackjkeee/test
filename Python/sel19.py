X = 99
def f1():
    X = 88
    def f2():
        X = 77
        print(X)
    f2()
    print(X)
f1()