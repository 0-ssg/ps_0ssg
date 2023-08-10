import sys

input = sys.stdin.readline

N= int(input())

arr = list(map(int, input().split()))

L = arr[0]
S = arr[0]

for i in range(N):
    if arr[i] > L:
        L = arr[i]
    elif arr[i] < S:
        S = arr[i]
print(S,L)
