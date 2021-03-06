n, m = map(int, input().split())

data = list(map(int, input().split())) #각 공별 수

balls = [0] * (11)

for i in data:
    balls[i] += 1

count = 0
for i in range(m+1):
    n -= balls[i] #같은 무게, 이전 무게 제외
    count += (n * balls[i]) #해당 수 곱해줌(같은 무게 다른공으로 치므로)

print(count)