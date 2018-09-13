def edit(line):
    ans = line.split(' ')
    result = ""
    cnt = 0
    for i in ans:
        cnt += 1
        if cnt == len(ans):
            result += i
        else:
            result += i
            result += "-"
    return result