import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for i in range(N):
    word = input()
    check = True
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            check = False
            break
    
    if check:
        cnt += 1
print(cnt)
