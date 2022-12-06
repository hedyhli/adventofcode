# 83
s=input()
for l in 4,14:print([i for i in range(4096)if len({*s[i:i+l]})==l][0]+l)

# 133 - regex
import re
s=input()
for n in 3,13:l="";print(re.search(("".join("(.)(?!%s)"%(l:=l+f"\\{i+1}|")[:-1]for i in range(n)))+".",s).end())
