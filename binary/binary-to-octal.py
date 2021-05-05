print "Enter a Binary Number:"
bnum = input()
rem = len(str(bnum)) % 3

binaryStr = str(bnum)
if rem == 2:
    binaryStr = "0" + binaryStr
if rem == 1:
    binaryStr = "00" + binaryStr

index = 0
octalCandidates = []
octalIndex = 0
while index < len(binaryStr):
    var = binaryStr[index: index + 3]
    octalCandidates.insert(octalIndex, var)
    octalIndex = octalIndex + 1
    index = index + 3

octalNumber = ''
for i in range(len(octalCandidates)):
    abc = octalCandidates[i]
    #print abc
    octalNumber = octalNumber + str(2 * 2 * (int(abc[0])) + 2 * 1 * (int(abc[1])) + int(abc[2]))

print "Octal Number is :", octalNumber
