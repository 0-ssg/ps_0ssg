# import sys
# input = sys.stdin.readline

S = input().rstrip()
a = [-1] * 26 

for i in range(len(S)):
    if a[ord(S[i]) - ord('a')] == -1:
        a[ord(S[i]) - ord('a')] = i
# a 들어오면 a - a = 0 >> a[0] = 0
# b 들어오면 b - a = 1 >> a[1] = 1 ...

for i in a:
    print(i, end=' ')