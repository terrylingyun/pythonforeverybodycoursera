def computepay(h,r) :
    if h <= 40 :
        return h * r
    else :
        return (40 * r) + ((h - 40) * (r * 1.5))

hours = input('How long did you work?')
rate = input('How much do you earn per hour?')
hours = float(hours)
rate = float(rate)

print('Pay', computepay(hours,rate))
