# Compound Interest

deposited = float(input('How much are you will deposit?'))

first_year = deposited + deposited * 0.04
second_year = first_year + first_year * 0.04
third_year = second_year + second_year * 0.04

print(f'In the first year, your final amount will be R$ {first_year:.2f}')
print(f'In the second year, your final amount will be R$ {second_year:.2f}')
print(f'In thr third year, your final amount will be R$ {third_year:.2f}')
