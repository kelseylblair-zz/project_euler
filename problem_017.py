# one + two + three + four + five = 19

NUMBER = 5

lengths = {
    1: len("one"), 
    2: len("two"), 
    3: len("three"), 
    4: len("four"), 
    5: len("five"), 
    6: len("six"), 
    7: len("seven"), 
    8: len("eight"), 
    9: len("nine"), 
    10: len("ten"), 
    11: len("eleven"), 
    12: len("twelve"), 
    13: len("thirteen"),
    14: len("fourteen"),
    15: len("fifteen"),
    16: len("sixteen"), 
    17: len("seventeen"),
    18: len("eighteen"),
    19: len("nineteen"),
    20: len("twenty"),
    30: len("thirty"),
    40: len("forty"),
    50: len("fifty"),
    60: len("sixty"),
    70: len("seventy"),
    80: len("eighty"),
    90: len("ninety"),
}

HUNDRED = len("hundred")
THOUSAND = len("thousand")
AND = len("and")

#----------

total = 0

for x in xrange(1, NUMBER + 1):
    s = str(x)
    l = len(s)
    place = l

    if l == 4:
        total += lengths[1]
        total += THOUSAND

    if l == 3 and int(s[l-3]) != 0:
        total += lengths[int(s[l-3])]
        total += HUNDRED
        if not (int(s[l-2]) == 0 and int(s[l-1]) == 0):
            total += AND
            place = 2
        else:
            place = 0
    if l == 2 or place == 2:
        if int(s[l-2]) == 1:
            total += lengths[int(s[l-2:])]
        elif int(s[l-2]) != 0:
            total += lengths[int(s[l-2]) * 10]
            place = 1
    if l == 1 or place == 1:
        if int(s[l-1]) != 0:
            total += lengths[int(s[l-1])]

print total


# cases:
# 1-digit = find in list and add
# 2-digit = either teens (find in list and add) 
#           or upper ten, may have ones digit
#           if tens digit = 1, find in list, otherwise parse & drop down
# 3-digit = need to parse out first digit, then add hundredn, maybe add and
#           then drop down to the 2-digit
# 4-digit = for this problem, 1000, but maybe worth parsing anyway for completion










