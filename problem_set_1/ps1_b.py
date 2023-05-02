annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual-raise, as a decimal: "))

portion_down_payment = 0.25
investiments_return = 0.04

current_savings = 0.0
number_of_months = 0

while current_savings < (total_cost * portion_down_payment):
    current_savings += current_savings * investiments_return / 12
    current_savings += (annual_salary / 12) * portion_saved
    number_of_months += 1
    
    if number_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

print("Number of months:", number_of_months)