import re
def is_done1(s):
    return s == 'done' or s == 'quit' 
def is_done2(s):
    return re.match('done|quit', s) != None

