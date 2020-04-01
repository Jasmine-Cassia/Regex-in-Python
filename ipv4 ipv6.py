import re
ipv4 = r"[0-9]{3}\.[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}"
ipv6 = r"([0-9A-Za-z]{4}:){7}[0-9A-Za-z]{4}"
data = "2001:0db8:0000:000:0000:ff00:0042:8329"
if re.match(ipv6,data):
    print("yes")
else:
    print("No")
