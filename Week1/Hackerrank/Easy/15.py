def edit__string(string, position, character):
    a = list(string)
    a[position] = character
    now = ""
    for i in a:
        now += i
    return str(now)