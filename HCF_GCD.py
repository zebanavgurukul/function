gcd = int(raw_input("enter your gcd number:) "))
hcf = int(raw_input("enter your hcf number :) "))
while gcd != hcf:
    if gcd > hcf:
        gcd = gcd - hcf
    else:
        hcf = hcf - gcd
print gcd
