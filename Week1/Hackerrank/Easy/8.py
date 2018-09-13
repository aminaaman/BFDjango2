n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
max1 = -100
for i in range(n):
    if a[int(i)] > maxi1:
        maxi1 = a[i]
max2 = -100
for i in range(n):
    if a[i] > max2 and a[i] != max1:
        max2 = a[i]
print(max2)