#
# Problem set 7 B part
#
import random

def roll5dice():
    result = []
    for die in range(5):
        result.append(random.randrange(1, 7))

    return result

def simulateDice(times = 1):
    sixes = []
    for time in range(times):
        throw = roll5dice()
        sixes.append(throw.count(6))

    return sixes

# Test
timesIn10000 = []
for i in range(100):
    timesIn10000.append( simulateDice(10000).count(5) )

mean = sum(timesIn10000)/float(len(timesIn10000))/10000
print mean
# 0.000121

print 1.0/6**5
# 0.0001286008230452675
