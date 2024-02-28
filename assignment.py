#Current tax rates in Kenya
#(0 - 240,000 KES, Rate: 10%)
#(240,001 - 400,000 KES, Rate: 25%)
#(400,001 - 800,000 KES, Rate: 30%)
#(800,001 KES and above, Rate: 35)
def calculate_tax(salary):
    if salary <= 240000:
        tax = salary * 0.10
    elif salary <= 400000:
        tax = (240000 * 0.10) + ((salary - 240000) * 0.25)
    elif salary <= 800000:
        tax = (240000 * 0.10) + (160000 * 0.25) + ((salary - 400000) * 0.30)
    else:
        tax = (240000 * 0.10) + (160000 * 0.25) + (400000 * 0.30) + ((salary - 800000) * 0.35)
    return tax

# Defining salary scenario
salary = 800000

# Calculate tax
tax_amount = calculate_tax(salary)

# Display the tax amount
print(f"For a salary of {salary} KES, the tax amount is: {tax_amount} KES")
