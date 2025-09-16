s = input()

find = 0
sind = 0

for i in range(len(s)):
    if s[i].isupper():
        find = i
        break

for j in range(1,len(s)):
    if s[j - 1].isdigit() and s[j].isdigit() == False:
        sind = j
        break

ans = ''
for g in range(find, len(s), sind - find):
    ans += s[g]

print(ans)