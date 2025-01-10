import math

cards = [13, 11, 10, 7, 4, 3, 1, 0]

def findNum(x, arr):
    length = len(arr)
    curridx = (length - 1) // 2
    upBound = length - 1
    lowBound = 0
    if x == arr[upBound]: return upBound
    if x == arr[0]: return 0
    while x != arr[curridx]:
        if x > arr[curridx]:
            upBound = curridx
            curridx = int((curridx + lowBound) / 2)
        elif x < arr[curridx]:
            lowBound = curridx
            curridx = int((curridx + upBound) / 2)
    return curridx



def bestSoln(x, arr):
    curridx = 0
    for i in arr:
        if x == i:
            return curridx
        curridx += 1
    return -1


soln = bestSoln(1, cards)

#dictionary: key,value pairs
test = {
    'input': {
        'x': 13,
        'arr': [13, 11, 10, 7, 4, 3, 1, 0]
    },
    'output' : 0
}

tests = []
tests.append(test)
tests.append({
    'input': {
        'x': -127,
        'arr': [3, -1, -9, -127]
    },
    'output' : 3
})

tests.append({
    'input': {
        'x': -9,
        'arr': [3, -1, -9, -127]
    },
    'output' : 2
})

tests.append({
    'input': {
        'x': -11,
        'arr': [3, -1, -9, -127]
    },
    'output' : -1
})

for i in tests:
    print(bestSoln(**i['input']) == i['output'])


#print(bestSoln(**test['input']) == test['output'])

def locate_cards(x, arr):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            hi = mid - 1
        elif x < arr[mid]:
            low = mid + 1
    return -1

