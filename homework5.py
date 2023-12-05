fourDigitNumber = int(input('Enter the four-digit number >>> '))
contraryNumber = (fourDigitNumber % 10 * 1000) + (fourDigitNumber // 10 % 10 * 100) + (fourDigitNumber // 100 % 10 * 10) + (fourDigitNumber // 1000)
print('The contrary number = ', contraryNumber)