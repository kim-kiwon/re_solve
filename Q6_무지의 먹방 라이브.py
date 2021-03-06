#직접 빼줄 필요가 없이 계산만 해줘야 시간초과 방지가능.
food_times = [3, 1, 2]
k = 5
INF = int(1e9)
import heapq

def solve(food_times, k):
    if k >= sum(food_times):
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, [food_times[i], i+1])

    sum_val = 0
    prev = 0
    length = len(food_times)
    #sum_val을 통해 k를 초과하는지 검사만 해준다.
    #food_times 같은 음식 있어도 now-prev가 0이되어 sum_val은 증가하지않고 제거 가능.
    while True:
        if (sum_val + (q[0][0] - prev) * length) > k:
            break
        now = heapq.heappop(q)[0]
        sum_val += (now - prev) * length
        length -= 1
        prev = now

    q.sort(key = lambda x : x[1])
    return q[(k-sum_val) % length][1]

print(solve(food_times, k))