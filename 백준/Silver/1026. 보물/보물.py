n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

result = 0

A = sorted(A)
C = sorted(B,reverse =True)
for i in range(n):
    result+=A[i]*C[i]
print(result)