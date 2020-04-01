import re
txt = "The rain in Covai"
x = re.search(r"\bC\w+",txt)
if x:
    print(x.span())
else:
    print(x)

