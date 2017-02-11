# Use the file name mbox-short.txt as the file name
#fname = raw_input("Enter file name: ")
fname2 = 'mbox-short.txt'
fh = open(fname2)
count = 0
x = 0
for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
       	count = count + 1
        x = float(line[19:26]) + x
    
print "Average spam confidence: ", x/count



