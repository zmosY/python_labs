n = int(input())
tcnt = 0
fcnt = 0

for _ in range (n):
    a,b,c,d = input().split()
    if d == 'True':
        tcnt += 1
    else:
        fcnt += 1

print(tcnt, fcnt)

