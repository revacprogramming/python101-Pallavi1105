name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()
for line in handle:
    if "From:" in line:
        continue
    if "From" in line:
        word_split = line.split()
        hour = word_split[5].split(":")[0]
        dic[hour] = dic.get(hour,0)+1

data =sorted([(v,k) for k,v in dic.items()],reverse=True)
lst =list()
for a,b in data:
    lst.append([b,a])
for a,b in sorted(lst):
    print(a,b)
