import re
txt = "The rain in India"
x = re.search("\s",txt)
print("First space index : ",x.start())
