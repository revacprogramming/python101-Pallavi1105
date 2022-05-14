def computepay(h, r):
  if h>40:
    p=1.5*r*(h-40)+(40*r)
  else:
    p=h*r
  return p
hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))
p = computepay(hrs, rte)
print("Pay", p)
