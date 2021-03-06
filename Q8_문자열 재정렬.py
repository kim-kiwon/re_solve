s = input()

alphas = []
numbers = 0

for x in s:
    # s[i]로 하지말고 원소 하나하나로 하자.
    if x.isdigit():
        numbers += int(x)
    else:
        alphas.append(x)

alphas.sort()
alphas = "".join(alphas)
print(alphas + str(numbers))