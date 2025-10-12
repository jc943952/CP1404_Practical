def main():
    income = []
    number_of_months =  int(input('how many months'))

    for month in range(1,number_of_months + 1):
        incomes = float(input('how much income was made?'))
        income.append(incomes)

    print_report(income)
    total = 0
    for month in range(1, number_of_months + 1):
            incomes += income[month - 1]
            total += incomes
            print("month: {:2} - income:{:10.2f} --> Total: ${:10.2f}".format(month, incomes, total))

def print_report(income):
    print("income report")
    total = 0
    for months, income in enumerate(income, 1):
        total += income
        print(f"month: {months}, income: {income:.2f} --> Total: {total:.2f}")

main()