from itertools import combinations
def findInd(s,target):
    sums = []
    for i in s:
        if type(i) != int: return False
    for i in combinations(s,2):
        if sum(c for c in i) == target : return s.index(i[0]), s.index(i[1])
    return 0
def findInd2(s,target):
    for i in s:
        if type(i) != int: return False
    for i in range(0,len(s)):
        for i2 in range(0,len(s)):
            if i == i2: continue
            if s[i]+s[i2] == target: return (i,i2)
    return 0
print(findInd([2,7,11,13],9))
print(findInd2([2,7,11,13],9))