# Function for Yearly Simple Interest
def yearly(p, r, t):
    si = (p * r * t) / 100
    return si

# Function for Half-Yearly Simple Interest
def half_yearly(p, r, t):
    si = (p * r * t) / 100
    return si

# Function for Quarterly Simple Interest
def quarterly(p, r, t):
    si = (p * r * t) / 100
    return si


# Main Program
p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time in Years: "))

print("\n--- Simple Interest ---")

print("Yearly Interest:", yearly(p, r, t))
print("Half-Yearly Interest:", half_yearly(p, r, t))
print("Quarterly Interest:", quarterly(p, r, t))
