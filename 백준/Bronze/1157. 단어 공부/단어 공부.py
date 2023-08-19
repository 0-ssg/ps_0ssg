N = input()
N = N.upper()

count = {}
for i in N:
    try:
        count[i] += 1
    except:
        count[i] = 1

max_cnt = max(count.values())

result = []
for a, b in count.items():
    if b == max_cnt:
        result.append(a)

if len(result) > 1:
    print("?")
else:
    print(result[0])
