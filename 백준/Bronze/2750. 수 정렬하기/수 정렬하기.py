num = int(input())
num_list = []
for i in range(num):
    num_list.append(int(input()))

sorted_list = sorted(set(num_list))

for i in sorted_list:
    print(i)
