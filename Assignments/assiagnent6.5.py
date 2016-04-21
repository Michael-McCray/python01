text = "X-DSPAM-Confidence:    0.8475"
x  = text.find(' ')
num = text[x+3:]
print num