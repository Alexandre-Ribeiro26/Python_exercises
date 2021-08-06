# Tax and Tip

meal = float(input('How much did your meal cost?'))

tax = float(meal * 0.12)
tip = float(meal * 0.18)

total_meal = float(meal + tax + tip)

print(f'The tax is R$ {tax:.2f}')
print(f'The tip is R$ {tip:.2f}')
print(f'The total of your meal is R$ {total_meal:.2f}')
