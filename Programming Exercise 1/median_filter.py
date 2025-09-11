from statistics import median

def median_filter(x):
    y = []
    for n in range(len(x)):
        if n == 0:
            window = [x[n], x[n], x[n+1]]
        elif n == len(x)-1:
            window = [x[n-1], x[n], x[n]]
        else:
            window = [x[n-1], x[n], x[n+1]]
        y.append(median(window))
    return y

# Test signals
x1 = [0, 0, 100, 0, 0]
x2 = [0, 1, 0, 0, 0]

# Apply system
Sx1 = median_filter(x1)
Sx2 = median_filter(x2)
Sx1_plus_x2 = median_filter([a+b for a, b in zip(x1, x2)])
Sx1_plus_Sx2 = [a+b for a, b in zip(Sx1, Sx2)]

print("S(x1)      =", Sx1)
print("S(x2)      =", Sx2)
print("S(x1+x2)   =", Sx1_plus_x2)
print("S(x1)+S(x2)=", Sx1_plus_Sx2)

# System properties discussion
print("\nSystem Properties:")
print("Linearity: No (since S(x1+x2) != S(x1)+S(x2))")
print("Time-Invariant: Yes (shifting input shifts output)")
print("Causal: Yes (output depends only on past and present inputs)")
print("Stable: Yes (bounded input gives bounded output)")