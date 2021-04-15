class demo:
    def method1(self):
        print("this is felix class")

    class user:
        def method2(self):
            print("this is me ")
d=demo()
d.method1()

d1=demo.user()
d1.method2()
