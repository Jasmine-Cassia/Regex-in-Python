import re
data = "ram is my name and ram@gmail.com and ram@yahoo.com"
list1 = re.findall(r"\S+@\S+", data)
if list1 == []:
    print("No")
else:
    print(*list1)
