print "Enter a Binary Number:"
binary_num = input()
rem = len(str(binary_num)) % 3

binaryStr = str(binary_num)
if rem == 2:
    binaryStr = "0" + binaryStr
if rem == 1:
    binaryStr = "00" + binaryStr

index = 0
octalCandidates = []
octalIndex = 0
decimalNumber = 0

strLength = len(binaryStr)
j = 1
for i in binaryStr:
    bitPosition = strLength - j
    # print "position :", bitPosition
    decimalNumber = decimalNumber + int(i) * (2 ** bitPosition)
    j = j + 1

print "Decimal Number is :", decimalNumber
