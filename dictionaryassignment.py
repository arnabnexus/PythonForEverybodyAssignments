name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    if line.startswith('From '):
        counts[line.split()[1]]=counts.get(line.split()[1],0)+1
maxkey=None
maxvalue=0
for key,value in counts.items():
    if maxkey==None or value>maxvalue:
        maxkey=key
        maxvalue=value
        
print(maxkey,maxvalue)