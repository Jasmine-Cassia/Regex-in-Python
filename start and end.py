import re
text = "The test will happen soon"
x = re.match("^The.*soon$",text)
if x:
    print("Match found!")
else:
    print("No match found!")
