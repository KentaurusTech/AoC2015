file = open('Day 5/input.txt')
pairs = []

def getIndex(item, items):
    index = -1
    for element in items:
        index += 1
        if (element == item):
            return index
    return -1

def check(str):
    cond1 = False
    oneBack = 'a'
    twoBack = 'b'
    threeBack = 'c'
    first = True
    second = True
    third = True
    pair = 'c'
    
    for c in str:
        if (first):
            pair = c
        else:
            pair = oneBack + c
        
        # sameOneAway = first == False and second == False and 
        passFirstCharacters = first == False and second == False and third == False 
        cond1Part1 = pair == threeBack + twoBack
        if (passFirstCharacters and cond1Part1):
            cond1 = True
        if (passFirstCharacters and cond1Part1 == False and getIndex(pair, pairs) != -1):
            cond1 = True

        if (first):
            first = False
        else:
            if (second):
                second = False
            elif (third):
                third = False
            pairs.append(pair)
        #shift letters
        threeBack = twoBack
        twoBack = oneBack
        oneBack = c
    return cond1

# count = 0
# for str in file:
#     if (check(str)):
#         count += 1
# print(count)
# print(check('qjhvhtzxzqqjkmpb'))
# print(check('xxyxx'))
# print(check('uurcxstgmygtbstg'))
# print(check('ieodomkazucvgmuy'))

print(check('aabcdefgaa')) # True
print(check('aaabcdefga')) # False
print(check('aaaabcdefg')) # True