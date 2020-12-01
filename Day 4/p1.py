from hashlib import md5
from itertools import count

for x in count(1):
    test = 'yzbqklnj' + str(x)
    if md5(test.encode('utf-8')).hexdigest()[:5] == '00000':
        print(x)
        break