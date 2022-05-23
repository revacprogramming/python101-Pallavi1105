def input():
    text = "X-DSPAM-Confidence:    0.8475"
    return text
def convert(text):
    a=text.find(':')
    b=text[a+1:]
    c=float(b)
    return c
def output(c):
    print(c)
def main():
    text=input()
    c=convert(text)
    output(c)
main()
