def compress(s, step):
    count = 1
    prev = s[:step]
    compressed = ""
    for i in range(step, len(s), step):
        cur = s[i : i + step]
        if cur == prev:
            count += 1
        else:
            compressed += (str(count) + prev) if count > 1 else prev
            count = 1
            prev = cur

    compressed += (str(count) + prev) if count > 1 else prev
    return len(compressed)


def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compress_length = compress(s, step)
        answer = min(answer, compress_length)
    return answer


print(solution("abcabcabcabcdededededede"))  # 14
