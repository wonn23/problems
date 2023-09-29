n = int(input())

weight = []
max_weight = 0
for i in range(n):
    weight.append(int(input()))
weight.sort()

for i in range(1,n+1):
    max_weight = max(max_weight, i * weight[n-i])
print(max_weight)