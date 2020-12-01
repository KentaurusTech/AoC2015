file = open('Day 5/input.txt')
bad = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']

def getIndex(item, items):
    index = -1
    for element in items:
        index += 1
        if (element == item):
            return index
    return -1

def check(str):
    cond1 = False
    cond2 = False
    vowelCount = 0
    previousChar = 'z'
    first = True
    pair = 'aa'
    for c in str:
        if (first):
            pair = c
        else:
            pair = previousChar + c

        if (getIndex(pair, bad) != -1):
            return False
        if (first == False and previousChar == c):
            cond2 = True
        if (getIndex(c, vowels) > -1):
            vowelCount += 1
            cond1 = vowelCount >= 3
        first = False
        previousChar = c
    return cond1 and cond2

count = 0
for str in file:
    if (check(str)):
        count += 1
print(count)
print(check('ugknbfddgicrmopn'))
print(check('aaa'))
print(check('haegwjzuvuyypxyu'))
print(check('jchzalrnumimnmhp'))
print(check('dvszwmarrgswjxmb'))