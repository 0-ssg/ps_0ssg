X = int(input())
N = int(input())
sum = 0
for i in range(N):
    money, cnt = map(int, input().split())
    sum +=  money *cnt
if (sum ==X):
     print("Yes")
else:
     print("No")