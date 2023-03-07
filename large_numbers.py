N, M, K = map(int,input().split())
List = list(map(int,input().split()))
List = sorted(List,reverse=True)
first = List[0]
second = List[1]

# 가장 큰 수가 더해지는 횟수 계산
count = M//(K+1)*K
count += M%(K+1)

result = 0
result += count*first # 가장 큰 수 더하기
result += (M-count)*second # 두 번째로 큰 수 더하기
print(result)