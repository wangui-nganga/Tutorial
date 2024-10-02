name = "Dave"
count = 1

def another():
    color = "blue"
    global count
    count += 1
    print(count) 

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("dave")

another()
# kuna global scope na local scope(function within a function)
# so the local for this example ni another alafu  global ni greeting

