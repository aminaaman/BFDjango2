def wrap(string, max_width):
    cnt = 0
    cur = ""
    for i in range(len(string)):
        cur = cur + string[i]
        cnt = cnt + 1
        if cnt == max_width:
            cur = cur + "\n"
            cnt = 0
    return cur