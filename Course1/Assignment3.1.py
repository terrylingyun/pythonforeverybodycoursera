hours = input('How long did you work?')
rate = input('How much do you get per hour?')
hours = float(hours)
rate = float(rate)
if hours <= 40 :
    pay = hours * rate
else :
    pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
print(pay)
