Optimization Problems and Algorithms
====================================

### Trajectory of Projectiles

How to calculate the goodness of a fit - cooefficient of determination.

`R**2 = 1 - EE/MV` - if `R**2` = 1, this explains all the change in the data. If `R**2` that means there is no relation between the model and the data, I.e. it is worthless.

```Python
def rSquare(measured, estimated):
    """measured: one dimensional array of measured values
       estimate: one dimensional array of predicted values"""
    EE = ((estimated - measured)**2).sum()
    mMean = measured.sum()/float(len(measured))
    MV = ((mMean - measured)**2).sum()
    return 1 - EE/MV
```

The plot of a projectile:

![plotted projectile](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/trajectory-of-projectile.png)

This shows that a quadratic fit is a very good model of reality for projectiles, because the `R**2` is 0.9858.

The whole purpose of creating a model is to be able to answer question about the physical situation.

In this example of a projectile, we have this theory behind it:

![slide 1](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/slide-1.png)

From here we know the formula of the parabola and that the vertical peak is at the middle of the x-axis.

Also we can tell how long it will take for the arrow to go from the peak to the target.

Using Python we get the following function:

```Python
def getXSpeed(a, b, c, minX, maxX):
    """minX and maxX are distances in inches"""
    xMid = (maxX - minX)/2.0
    yPeak = a*xMid**2 + b*xMid + c
    g = 32.16*12 #accel. of gravity in inches/sec/sec
    t = (2.0*yPeak/g)**0.5
    return xMid/(t*12.0)
    #print 'speed = ' + str(int(xMid/(t*12))) + ' feet/sec'
```

A very common pattern in science and engineering

1. Started with an experiment (this gave us some data)
2. Then used computation to both find and evaluate a model of the actual physical system
3. Used some theory and analysis and computation to derive a consequence of a model

### Optimization Problems

Not so much in the sense how to make a program fast, but more so about optimization problems. Every problem we're going to look at will have to parts:

1. An objective function (either maximized or minimized)
2. A set of constraints that have to be satisfied

There are a lot of classic optimization problems that people have worked for decades. One useful technique in solving problems is finding the best classic problem and map your problem to its solution. This is know as problem reduction.

One thing to look at is how long does it take to solve. These problems are typically without an efficient computational way to solve them.

#### 0/1 Knapsack Problem

The really hard problem a burglar is the decision what to steal. He has a limited bagpack, he has to maximise what to steal subject to weight restrictions.

You have a table of items/value/weight values. The simplest solutions is the greedy algorithm.

#### The Greedy Algorithm

They are very popular and often the right way to tackle a problem. They are iterative and at each step choose locally optimal solutions.

That assumes that at each stage we know the locally optimal solution. There are a few ways you can think of evaluating the next optimal choice:

1. Pick the biggest value item at each step
2. Pick the lowest weight items each step
3. Pick the best value to weight ratio items each step

In fact none of these methods would consistently give you the best outcome. This is one of the issues of the greedy algorithm. This knapsack problem is specifically called the 0/1 version because you can either take the whole item of leave it. The continous knapsack problem can be fully solved by the greedy algorithm.

```Python
def greedy(Items, maxWeight, keyFcn):
    assert type(Items) == list and maxWeight >= 0
    ItemsCopy = sorted(Items, key=keyFcn, reverse = True)
    result = []
    totalVal = 0.0
    totalWeight = 0.0
    i = 0
    while totalWeight < maxWeight and i < len(Items): # >
        if (totalWeight + ItemsCopy[i].getWeight()) <= maxWeight:
            result.append((ItemsCopy[i]))
            totalWeight += ItemsCopy[i].getWeight()
            totalVal += ItemsCopy[i].getValue()
        i += 1
    return (result, totalVal)
```

The test harnesses for this function

```Python
def testGreedy(Items, constraint, getKey):
    taken, val = greedy(Items, constraint, getKey)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print '  ', item

def testGreedys(maxWeight = 20):
    Items = buildItems()
    print('Items to choose from:')
    for item in Items:
        print '  ', item
    print 'Use greedy by value to fill a knapsack of size', maxWeight
    testGreedy(Items, maxWeight, value)
    print 'Use greedy by weight to fill a knapsack of size', maxWeight
    testGreedy(Items, maxWeight, weightInverse)
    print 'Use greedy by density to fill a knapsack of size', maxWeight
    testGreedy(Items, maxWeight, density)
```

This produces this result:

```
Items to choose from:
   <clock, 175.0, 10.0>
   <painting, 90.0, 9.0>
   <radio, 20.0, 4.0>
   <vase, 50.0, 2.0>
   <book, 10.0, 1.0>
   <computer, 200.0, 20.0>
Use greedy by value to fill a knapsack of size 20
Total value of items taken = 200.0
   <computer, 200.0, 20.0>
Use greedy by weight to fill a knapsack of size 20
Total value of items taken = 170.0
   <book, 10.0, 1.0>
   <vase, 50.0, 2.0>
   <radio, 20.0, 4.0>
   <painting, 90.0, 9.0>
Use greedy by density to fill a knapsack of size 20
Total value of items taken = 255.0
   <vase, 50.0, 2.0>
   <clock, 175.0, 10.0>
   <book, 10.0, 1.0>
   <radio, 20.0, 4.0>
```

The efficiency of this code?

What this algo does:

1. Sorts the list - `O(len(items) * log(len(items))`
2. Loops the list - `O(len(items))`

So this algo has the complexity of `O(n * log(n))`. Greedy algorithms are often very close to linear so that's why they are considered efficient.

#### Finding the Optimal Solution

The important thing here is not the solution to the problem, but the process used to define the problem. A careful formulation of the problem often reveals how to solve it.

1. Represent each item by a pair = `<value, weight>`
2. `W` as max.weight the thief can carry
3. Represent the set of available items as a vector - `I`
4. Have another vector `V` which indicates whether or not each item in `I` is taken.
    - if `V[i] = 1` then `I[i]` has been taken
    
Having formulated the situation, we can now come back to the optimisation problem.

The objective function - maximize `sum(V[i]*I[i].value)`.
Subject to the constraint - `sum(V[i]*I[i].weight) <= W`.

#### Expected Run﻿ Times

What would the most straight forward implementation would look like?

The brute force solution:

1. Enumerate all possibilities
2. Choose the best that meets the constraint

The question is how long is this going to run? It depends on how big the set of items is. If we have `n` times, the vector can take on `2**n` values. So this means this has `O(2**n)`.

We have to find something better to be able to solve this on a bigger scale.
