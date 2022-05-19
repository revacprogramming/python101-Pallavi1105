def computepay(h, r):
  if h>40:
    p=1.5*r*(h-40)+(40*r)
  else:
    p=h*r
  return p
def output(p):
  print("pay:",p) 
def main():
  h = float(input("Enter hours? "))
  r = float(input("Enter rate per hour? "))
  p = computepay(h, r)
  output(p)
main()

