name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dicthourfrequency=dict()
for line in handle:
    if line.startswith('From '):
        dicthourfrequency[(line.split()[5]).split(':')[0]]=dicthourfrequency.get((line.split()[5]).split(':')[0],0)+1
        
for k,v in sorted(dicthourfrequency.items()):
    print(k,v)

