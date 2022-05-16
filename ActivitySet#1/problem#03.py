def Earning(hrs,rate):
  wage=hrs*rate
  return wage
def output(wage):
  print('Pay:',wage)
def main():
 hrs = float(input("Enter hours? "))
 rate=float(input("Enter Rate"))
 wage=Earning(hrs,rate)
 output(wage)
main()
