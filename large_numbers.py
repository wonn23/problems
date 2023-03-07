N, M, K = map(int,input().split())
List = list(map(int,input().split()))
List = sorted(List,reverse=True)
num=0
Sum = 0
i=0
while M-num >0:
    num+=1
    if i == K-1:
        i = 0
        Sum+=List[1]
    else:
        Sum+=List[0]
        i+=1
print(Sum)