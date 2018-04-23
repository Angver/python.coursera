import sys
digit_strings = sys.argv[1]

summa = 0
for digit in digit_strings:
    summa += int(digit)

print(summa)