import sys
input = sys.stdin.readline

a,b= map(int,input().split())

reverse_a = int(str(a)[::-1])
reverse_b = int(str(b)[::-1])

print(max(reverse_a, reverse_b))