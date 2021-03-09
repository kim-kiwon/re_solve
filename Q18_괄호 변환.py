p1 = "(()())()"
p2 = ")("
p3 = "())))((()"
p4 = ""
def check_proper(u):
    count = 0
    for i in range(len(u)):
        if u[i] == "(":
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    if p == '':
        return ''
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            break
    u, v = p[:i+1], p[i+1:]
    if check_proper(u):
        result = u + solution(v)
    else:
        result = "("
        result += solution(v)
        result += ")"
        u_val = u[1:-1]
        for i in range(len(u_val)):
            if u_val[i] == "(":
                result += ")"
            else:
                result += "("
    return result

print(solution(p1))