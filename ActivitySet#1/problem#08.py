fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
        
    else:
            count =count+1
            s=line.find('0')
            num=float(line[s:])
            total+=num
            
        
average=total/count
print('Average spam confidence:',average)




