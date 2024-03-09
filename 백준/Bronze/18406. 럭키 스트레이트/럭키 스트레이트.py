n = input()

a = list(map(int,n))
length = len(a)
if sum(a[:length//2]) == sum(a[length//2:]):
    print('LUCKY')
else:
    print('READY')