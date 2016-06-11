# one + two + three + four + five = 19

NUMBER = 5;

lengths = {
    1: 3, 
    2: 3, 
    3: 5, 
    4: 4, 
    5: 4, 
    6: 3, 
    7: 5, 
    8: 5, 
    9: 4, 
    10: 3, 
    11: 6, 
    12: 6, 
    13: 8,
    14: 8,
    15: 7,
    16: 7, 
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
}

HUNDRED = 7
THOUSAND = 8
AND = 3

#----------

total = 0

for x in xrange(1, NUMBER + 1):
    s = str(x)
    l = len(s)

    if l == 4:
        total += lengths(1)
        total += THOUSAND
    if l == 3:
        total += lengths(int(s[l-3]))
        total += HUNDRED
        if !(int(s[l-2]) == 0 && int(s[l-1]) == 0):
            total += AND
            l = 2
        else
            l = 0
    if l == 2:
        if int(s[l-2]) == 1:
            total += lengths(int(s[l-2:l-1]))


# cases:
# 1-digit = find in list and add
# 2-digit = either teens (find in list and add) 
#           or upper ten, may have ones digit
#           if tens digit = 1, find in list, otherwise parse & drop down
# 3-digit = need to parse out first digit, then add hundredn, maybe add and
#           then drop down to the 2-digit
# 4-digit = for this problem, 1000, but maybe worth parsing anyway for competion










