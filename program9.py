# def addtwo(a, b):
	# added = a + b
	# return a

# x = addtwo(2,7)
# print x

def computepay(h,r):
	if h > 40:
		oth = (h - 40)
		p = (40 * r) + (oth * 1.5 * r)
	if h <= 40:
		p = h * r
	return p

hrs = float(raw_input("Enter Hours:"))
rph = float(raw_input("Enter Rate Per Hour:"))
totalpay = computepay(hrs,rph)
print "Pay", totalpay