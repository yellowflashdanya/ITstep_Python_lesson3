fourDigit = int(input('Write a four-digit number >>> '))
product = (fourDigit // 1000) * (fourDigit // 100 % 10) * (fourDigit // 10 % 10) * (fourDigit % 10)
print('The number you get >>> ', product)