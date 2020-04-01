import re
data = input()
match_list = re.findall(r'\d+',data)
print(*match_list)
