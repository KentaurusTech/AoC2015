file = open('Day 3/input.txt').read()

def getIndex(item, items):
    index = -1
    for element in items:
        index += 1
        if (element == item):
            return index
    return -1

def getCoordDif(character):
    if (character == '^'):
        return [0, 1]
    if (character == '>'):
        return [1, 0]
    if (character == 'v'):
        return [0, -1]
    if (character == '<'):
        return [-1, 0]

def getProperCoord(index, coord1, coord2):
    if (index % 2 == 0):
        return coord1
    return coord2

def parseString(str):
    coord1 = [0, 0]
    coord2 = [0, 0]
    coordIndex = 0
    coord = [0, 0]
    houseCoords = []
    houseCount = []
    houseCoords.append(coord)
    houseCount.append(2)
    for item in str:
        movement = getCoordDif(item)
        coordIndex += 1
        coord = getProperCoord(coordIndex, coord1, coord2)
        coord[0] += movement[0]
        coord[1] += movement[1]
        index = getIndex(coord, houseCoords)
        if (index == -1):
            houseCoords.append(coord.copy())
            houseCount.append(1)
        else:
            houseCount[index] += 1
    print(len(houseCount))

parseString('<')
parseString('^>v<')
parseString('^v^v^v^v^v')
parseString(file)