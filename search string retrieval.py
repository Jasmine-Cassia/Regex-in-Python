import re
txt = "The rain in Covai"
x = re.search(r"\bC\w+",txt)
print(x.string)

