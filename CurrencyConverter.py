amount = float(input('Please enter the amount of money: \n>>'))
currencyFrom = input('Please enter the amount currency: \n>>')
dollarValues = ['d', 'D', 'dollar', 'Dollar', 'DOLLAR', 'usd', 'USD', '$']
euroValues = ['e', 'E', 'euro', 'Euro', 'EURO', 'eur', 'EUR', '€']
poundValues = ['p', 'P','pound', 'Pound', 'POUND', 'lb', 'LB', '£']
yenValues = ['y', 'Y', 'yen', 'Yen', 'YEN', 'jpy', 'JPY', '¥']
currencyTo = input('What curency would you like to convert it to? \n>>')

if currencyFrom in dollarValues and currencyTo in euroValues:
    converted = amount * 0.88
    print(amount, 'Dollar(s) is worth', converted, 'Euro(s).')
elif currencyFrom in dollarValues and currencyTo in poundValues:
    converted = amount * 0.74
    print(amount, 'Dollar(s) is worth', converted, 'Pound(s).')
elif currencyFrom in dollarValues and currencyTo in yenValues:
    converted = amount * 115.58
    print(amount, 'Dollar(s) is worth', converted, 'Yen.')
elif currencyFrom in euroValues and currencyTo in dollarValues:
    converted = amount * 1.14
    print(amount, 'Euro(s) is worth', converted, 'Dollar(s).')
elif currencyFrom in euroValues and currencyTo in poundValues:
    converted = amount * 0.84
    print(amount, 'Euro(s) is worth', converted, 'Pound(s).')
elif currencyFrom in euroValues and currencyTo in yenValues:
    converted = amount * 131.99
    print(amount, 'Euro(s) is worth', converted, 'Yen.')
elif currencyFrom in poundValues and currencyTo in dollarValues:
    converted = amount * 1.35
    print(amount, 'Pound(s) is worth', converted, 'Dollar(s).')
elif currencyFrom in poundValues and currencyTo in euroValues:
    converted = amount * 1.19
    print(amount, 'Pound(s) is worth', converted, 'Euro(s).')
elif currencyFrom in poundValues and currencyTo in yenValues:
    converted = amount * 156.55
    print(amount, 'Pound(s) is worth', converted, 'Yen.')
elif currencyFrom in yenValues and currencyTo in dollarValues:
    converted = amount * 0.0087
    print(amount, 'Yen is worth', converted, 'Dollar(s).')
elif currencyFrom in yenValues and currencyTo in euroValues:
    converted = amount * 0.0076
    print(amount, 'Yen is worth', converted, 'Euro(s).')
elif currencyFrom in yenValues and currencyTo in poundValues:
    converted = amount * 0.0064
    print(amount, 'Yen is worth', converted, 'Pound(s).')
else :
    print('Invalid value(s) selected. Please input from the following currencies: \n United States Dollar:', dollarValues, '\n Euro:', euroValues, '\n British Pound Sterling:', poundValues, '\n Japanese Yen:', yenValues)





