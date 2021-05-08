"""
Keep calling conversion function with n/2  till n > 1,
later perform n % 1 to get MSB of converted binary number.
Example :- 7
1). 7/2 = Quotient = 3(grater than 1), Remainder = 1.
2). 3/2 = Quotient = 1(not grater than 1), Remainder = 1.
3). 1%2 = Remainder = 1.
Therefore, answer is 111.
"""
print "Enter a Decimal Number:"
decimal_num = input()

quotient = 0
remainder = 0
binaryNumber = []
i = 0
while decimal_num >= 1:
    quotient = decimal_num / 2
    remainder = decimal_num % 2
    decimal_num = quotient
    binaryNumber.insert(i, remainder)
    i = i + 1

print binaryNumber
