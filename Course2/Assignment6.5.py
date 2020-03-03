text = "X-DSPAM-Confidence:    0.8475"
output = text.strip()
position = output.find(':')
output = output[position+1:]
output = float(output)
print(output)
