def demo1():
    print("demo1 method")
    def innerone():
        print("inner method 1")
        def innerTwo():
            print("inner method 2")
        innerone()
        innerTwo()
        demo1()