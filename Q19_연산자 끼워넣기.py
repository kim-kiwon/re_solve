#백트래킹 문제 -> 순열 조합으로 풀이 가능한 경우 많음.
import sys
n = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

min_val = sys.maxsize
max_val = -sys.maxsize

def solution(val, idx):
    global min_val, max_val
    if idx == len(nums):
        min_val = min(val, min_val)
        max_val = max(val, max_val)
        return
    if oper[0] > 0:
        oper[0] -= 1
        solution(val + nums[idx], idx + 1)
        oper[0] += 1
    if oper[1] > 0:
        oper[1] -= 1
        solution(val - nums[idx], idx + 1)
        oper[1] += 1
    if oper[2] > 0:
        oper[2] -= 1
        solution(val * nums[idx], idx + 1)
        oper[2] += 1
    if oper[3] > 0:
        oper[3] -= 1
        solution(int(val / nums[idx]), idx + 1)
        oper[3] += 1

solution(nums[0], 1)
print(max_val)
print(min_val)