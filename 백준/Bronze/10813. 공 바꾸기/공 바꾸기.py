import sys
input = sys.stdin.readline

# 바구니 >> 1~N개 바구니1엔 1번공 , 바구니2엔 2번공 ~~~ 바구니N엔 N번공
# 바꿀 횟수(M)주고 a,b바구니 공을 바꿈

N,M = map(int,input().split())

arr= []

for i in range(N):
    arr.append(i+1)
# print(*arr)

for i in range(M):
    a,b=map(int,input().split())
    temp = arr[a-1]
    arr[a-1] = arr[b-1]
    arr[b-1] = temp

print(*arr)
