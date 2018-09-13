if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    maxi = -100
    for i in arr:
        if i > maxi:
            maxi = i
    maxi2 = -100
    for i in arr:
        if i > maxi2 and i != maxi:
            maxi2 = i
    print(maxi2)