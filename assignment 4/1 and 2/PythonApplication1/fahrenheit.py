amountf = input("how many degrees in fahrenheit to celcius?")
pre = amountf
amountf = (amountf - 32.00) / 1.80
amountf = round(amountf, 2)

print "%s degrees fahrenheit is %s degrees celcius"  % (pre, amountf)
