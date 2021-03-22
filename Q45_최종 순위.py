t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n+1)]

    last_year = list(map(int, input().split())) #n번째 -> n번 등수인 팀

    indegree = [0] * (n+1)
    for i in range(len(last_year)):
        for j in range(-len(last_year) + 1 + i, 0):
            graph[last_year[i]].append(last_year[j])
            indegree[last_year[j]] += 1

    c = int(input())
    for _ in range(c):
        a, b = map(int, input().split())
        if b in graph[a]: #작년에 a팀 등수가 b팀보다 높았다.
            graph[a].remove(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] -= 1
        else: #작년에 a팀 등수가 b팀보다 낮았다.
            graph[b].remove(a)
            graph[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1
    q = []
    result = []
    flag = 0
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    for i in range(n):
        if len(q) == 0:
            print("IMPOSSIBLE")
            flag = 1
            break
        elif len(q) >= 2:
            print("?")
            flag = 1
            break
        checked = q.pop()
        result.append(checked)
        for i in graph[checked]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if flag == 0:
        for i in result:
           print(i, end = " ")
        print()
