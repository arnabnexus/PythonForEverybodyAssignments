# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
lineCount=0
totalSpamConfidence=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    totalSpamConfidence=totalSpamConfidence+float((line[line.find(':')+1:]).strip())
    lineCount=lineCount+1

print("Average spam confidence:",(totalSpamConfidence/lineCount))