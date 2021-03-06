s1 = "aabbacccc"
s2 = "ababcdcdababcdcd"
s3 = "abcabcdede"
s4 = "abcabcabcabcdededededede"
s5 = "xababcdcdababcdcd"

def solve(s):
    length = len(s)
    len_val = length
    for i in range(1, length // 2 + 1):
        result = []
        token = s[:i]
        count = 1
        for j in range(i, length, i):
            val = s[j:j+i]
            if token == val:
                count += 1
            else:
                if count != 1:
                    result.append(str(count) + token)
                else:
                    result.append(token)
                token = val
                count = 1
            if j == length - i:
                if count != 1:
                    result.append(str(count) + token)
                else:
                    result.append(token)
        if i + j > length:
            for k in range(j, length):
                result.append(s[k])
        result = "".join(result)
        len_val = min(len(result), len_val)
    print(len_val)

solve(s1)