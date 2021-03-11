n, x = map(int, input().split())

data = list(map(int, input().split()))

def find_left_idx(val):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end ) // 2
        if data[mid] == val:
            if mid == 0 or data[mid - 1] < val:
                return mid
            else: end = mid - 1
        elif data[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
    return None
def find_right_idx(val):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == val:
            if mid == len(data) - 1 or data[mid + 1] > val:
                return mid
            else:
                start = mid + 1
        elif data[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
    return None

l_val = find_left_idx(x)
r_val = find_right_idx(x)
if l_val == None:
    print(-1)
else:
    print(r_val - l_val + 1)