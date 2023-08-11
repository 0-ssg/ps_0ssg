# import sys
# input = sys.stdin.readline

S = input().rstrip()
a = [-1] * 26 

for i in range(len(S)):
    if a[ord(S[i]) - ord('a')] == -1:
        a[ord(S[i]) - ord('a')] = i

for i in a:
    print(i, end=' ')