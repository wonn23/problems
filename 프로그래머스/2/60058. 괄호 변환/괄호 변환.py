def solution(p):
    # 1. 빈 문자열인 경우
    if p == "":
        return ""

    # 2. 문자열을 두 균형잡힌 문자열 u, v로 분리
    def split_to_balanced(p):
        balance = 0
        # "(", ")"을 각각 세어서 수가 같은지 확인하는 것이 아니라 for문을 1회 사용하면서 balance가 0으로 수렴하는지 확인한다.
        for i in range(len(p)):
            if p[i] == "(":
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                # i 번째에 balance가 맞춰졌으면 p를 u,v로 나누어 return 한다.
                return p[: i + 1], p[i + 1 :]

    u, v = split_to_balanced(p)

    # 3. u가 올바른 괄호 문자열인지 확인
    def is_correct(u):
        stack = []
        for char in u:
            if char == "(":
                stack.append("(")
            else:
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0

    if is_correct(u):
        # 3.1 올바른 괄호 문자열이면 v에 대해 재귀 호출
        return u + solution(v)
    else:
        # 4. 올바르지 않을 경우
        result = "("
        result += solution(v)
        result += ")"
        u = u[1:-1]
        for char in u:
            result += ")" if char == "(" else "("
        return result
