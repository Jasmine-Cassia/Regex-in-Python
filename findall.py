import re
txt = "The rain in India"
x = re.findall("ai",txt)
print(x)

'''
import re
txt = "The rain in India"
x = re.findall("Spain",txt)
if x:
    print("Yes, there is atleast one match")
else:
    print("No match found!")
'''
