def mortgage_calculator():
    print("\n--- Mortgage Calculator ---")
    
    loan_amount = float(input("Enter the loan amount (₹): "))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    loan_term_years = int(input("Enter the loan term (in years): "))

    monthly_interest_rate = annual_interest_rate / 100 / 12
    total_payments = loan_term_years * 12

    if monthly_interest_rate == 0:
        monthly_payment = loan_amount / total_payments
    else:
        monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / \
                          ((1 + monthly_interest_rate) ** total_payments - 1)

    print(f"\nEstimated Monthly Mortgage Payment: ₹{monthly_payment:.2f}")


def investment_return_calculator():
    print("\n--- Investment Return Calculator ---")
    
    principal = float(input("Enter the initial investment amount (₹): "))
    annual_rate = float(input("Enter the expected annual rate of return (in %): "))
    time_years = int(input("Enter the investment time horizon (in years): "))

    rate_decimal = annual_rate / 100
    future_value = principal * (1 + rate_decimal) ** time_years

    print(f"\nEstimated Future Value of Investment: ₹{future_value:.2f}")


def savings_goal_calculator():
    print("\n--- Savings Goal Calculator ---")
    
    goal_amount = float(input("Enter your savings goal amount (₹): "))
    annual_rate = float(input("Enter the expected annual rate of return (in %): "))
    time_years = int(input("Enter the time frame to reach your goal (in years): "))

    monthly_rate = annual_rate / 100 / 12
    total_months = time_years * 12

    if monthly_rate == 0:
        monthly_contribution = goal_amount / total_months
    else:
        monthly_contribution = goal_amount * monthly_rate / ((1 + monthly_rate) ** total_months - 1)

    print(f"\nYou need to invest ₹{monthly_contribution:.2f} per month to reach your goal.")


def income_tax_calculator():
    print("\n--- Income Tax Calculator ---")

    income = float(input("Enter your annual income (₹): "))
    deductions = float(input("Enter total deductions (₹): "))

    taxable_income = max(0, income - deductions)
    tax = 0

    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = (250000 * 0.05) + (taxable_income - 500000) * 0.20
    else:
        tax = (250000 * 0.05) + (500000 * 0.20) + (taxable_income - 1000000) * 0.30

    print(f"\nEstimated Tax Payable: ₹{tax:.2f}")


def main_menu():
    while True:
        print("\n=== Financial Planning Toolkit ===")
        print("1. Mortgage Calculator")
        print("2. Investment Return Calculator")
        print("3. Savings Goal Calculator")
        print("4. Income Tax Calculator")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            mortgage_calculator()
        elif choice == '2':
            investment_return_calculator()
        elif choice == '3':
            savings_goal_calculator()
        elif choice == '4':
            income_tax_calculator()
        elif choice == '5':
            print("Exiting the toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
