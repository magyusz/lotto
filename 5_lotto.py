# 5-ös lotto:
import random
randomlist = []
szam = None
while len(randomlist) < 5:
    szam = random.randint(1,91)
    if szam not in randomlist:
        randomlist.append(szam)
    elif szam in randomlist:
        continue
print(sorted(randomlist))
