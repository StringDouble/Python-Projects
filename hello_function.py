name = 'Yoana'
def say_hello():
    print('Hello ' + name + '!' )
def change_name(new_name):
    global name
    name = new_name
