def solution(number, k):
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:
                stack.pop()
                k-=1
        stack.append(num)
    if k != 0: # "1111111" 이고 k=2 이면 while문에 못들어가고 계속 stack에 쌓인다.
        stack = stack[:-k]
    return ''.join(stack)
            