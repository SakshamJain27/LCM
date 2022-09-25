def multiple(number):
    multiples = []
    for i in range(2, 100):
        multiples.append(number*i)
    return (multiples)

number1 = multiple(int(input('Enter the first number:')))
number2 = multiple(int(input('Enter the second number:')))

print(min(set(number1).intersection(set(number2))))
