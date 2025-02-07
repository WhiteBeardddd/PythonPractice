price = 1000000

good_credit = False

if good_credit:
    down = 0.1 * price
else:
    down = 0.2 * price
    
print(f"Down payment: ${down}")