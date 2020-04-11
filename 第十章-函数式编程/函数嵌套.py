def func():
    choose = int(input("> "))
    def func1():
        print("func1")
    def func2():
        print("func2")
        def func2_1():
            print("func2.1")
    if choose == 1:
        func1()
    elif choose == 2:
        func2()
    print("func")
func()