def numnote(1st):
    msg = []
    for num in 1st:
        if num < 0:
            s = str(num) + ' is negative'
        elif 0 <= num <= 9:
            s = str(num) + ' is digit'
        msg.append(s)
    return msg
