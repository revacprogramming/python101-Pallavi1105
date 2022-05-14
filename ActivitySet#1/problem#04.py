hrs = input("Enter Hours:")
h = float(hrs)
xx =float(input("Enter the Rate:"))
if h <= 40:
 	print( h  * xx)
elif h > 40:
	print(40* xx + (h-40)*1.5*xx)

