a,b = map(int, input().split())
c = int(input())

h = int((b+c) / 60)
m = (b+c) % 60

hour = a+h 
if hour >= 24:
    hour -= 24

print(hour, m) 