import sys
input = sys.stdin.readline

arr= []

for i in range(30):
    arr.append(i+1)

for _ in range(28):
    n = int(input())
    arr.remove(n)

print(min(arr))
print(max(arr))


