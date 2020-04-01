import re
n = int(input())
d = {}
for i in range(n):
    temp = {}
    data = input()
    regno = re.findall(r"[7][0-9]{11}",data)
    name = re.findall(r"[A-Z]+", data)
    city = re.findall(r"\#w+", data)
    mob = re.findall(r"[7-9][0-9]{9}", data)
    if regno==[]:
        regno = ["null"]
    if name==[]:
         name = ["null"]
    if city == []:
        city = ["null"]
    if mob==[] or len(mob)==1:
        mob = ["null"]
    
    temp = {"name": name[0],"city": city[0],"mob":mob[-1]}
    d[int(regno[0])] = temp
print(d)
for k,v in sorted(d.items()):
    print(k,v["name"],v["city"],v["mob"])
