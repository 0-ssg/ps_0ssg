import sys

input = sys.stdin.readline

N,M=map(int,input().split())

arr =[0]*N

# 0 0 0 0 0
# 3 3 0 0 0
# 3 3 4 4 0
# 1 1 1 1 0
# 1 2 1 1 0

for i in range(M):
    # a번째 바구니부터 b번째 바구니까지 c 번호의 공을 넣음
    a,b,c = map(int,input().split())
    for j in range(a -1, b):
        arr[j]=c

for i in range(N):
 print(arr[i],end=" ")

