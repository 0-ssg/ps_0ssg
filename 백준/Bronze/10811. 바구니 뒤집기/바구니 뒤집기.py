import sys
input = sys.stdin.readline

# 바구니 >> 1~N개 바구니1엔 1번공 , 바구니2엔 2번공 ~~~ 바구니N엔 N번공
# 뒤집기 횟수(M)주고 a번째 바구니와 b번째 바구니역순  >> 1 4 >> 4 3 2 1 5
N,M = map(int,input().split())

arr= []

for i in range(N):
    arr.append(i+1)

for _ in range(M):
    a ,b = map(int,input().split())
    arr[a - 1:b] = reversed(arr[a - 1:b])
# 0 1 2 3 4
# 1 2 3 4 5
print(*arr)