Using Randomness to Solve Non-random Problems
=============================================

Last lecture ended with Gaussian distributions. The thing about the _Gaussian distribution_ is that you can fully characterize it by its mean and standard deviation.

How do we construct computational models that will help us understand the real world?

If something is not actually normally distributed, and we think it is, that can lead to very wrong outcomes.

### Uniform distributions

The Massachusets lottery has the probability of each number being the same. Such distributions are called **Uniform**, I.e. each result is equally probable. We can fully characterize this distribution only by its range.

They are most common in games devised by humans, but are not found in nature.

### Exponential distributions

They are used in a lot of different ways, for example highway planners use them to model how much of a gap is there between cars. They are **memoryless**.

Assume that at each time step each drug molecule has a probability `P` of being removed from the body. The fact that a molecule has not been cleared at time `t-1` will not have any effect on the probability of it being cleared at time `t`.

* `t = 1` - what is the probability of being still in the body? `1 - P`.
* `t = 2` - is it the same? `(1 - P)**2`
* `t = n` - `(1 - P)**n`

Suppose at `t = 0` there are `n` molecules.

```Python
def clear(n, clearProb, steps):
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n*((1-clearProb)**t))
    pylab.plot(numRemaining, label = 'Exponential Decay')
    
clear(1000, 0.01, 500)
pylab.semilogy()
pylab.ion()
pylab.show()
```

This produces this graph:

![log graph](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/clear-graph.png)

This is a straigh line because `y` axis is logarithmic, if we change it to the normal `y`, then the graph looks like this:

![non-log graph](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/clear-graph-non-log.png)

This does look like exponential decay, it asymptotes towards zero, but never gets there. To find out if you have an exponential distribution, put it on a log axis and see if its a straight line.

#### Monte Carlo example

Instead of knowing to look for `(1-P)**t`, we can use `random.random()`:

```Python
def clearSim(n, clearProb, steps):
    numRemaining = [n]
    for t in range(steps):
        numLeft = numRemaining[-1]
        for m in range(numRemaining[-1]):
            if random.random() <= clearProb: 
                numLeft -= 1
        numRemaining.append(numLeft)
    pylab.plot(numRemaining, 'r', label = 'Simulation')
```

![simulation vs mathematical](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/simulation-graph.png)

* Analytics model
* Simulation model

Both show exponential decay, but they're not identical. Which would we prefer? There is no right answer.

When we're thinking of evaluating a model, we have to ask questions:

1. Fidelity - credibility
3. Utility - what questions are answerable with the model

Because typically we don't know the answer when we're modeling, so the question is can we reason the results and see meaning in them.

In this case the simulation model offers additional utility, because it allows for **what if** questions. For example in case the molecules of the drug every `t=100` would clone themselves, it is clear what you need to do to model that with a simulation.

Using the simulation model to facilitate such molecules, we can quickly get this graph:

![every t=100 clone](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/every-100-clone.png)

Many physical systems exhibit exponential decay/growth.

### Monty Hall problem

There are three doors, behind one there is a prize. The contestant chooses one door, the MC opens a different door and shows a goat. Now he extends an offer to switch. What should be contestant do?

#### Analysis

After the contestant makes a choice, she has `1/3` chance that the car is behind her door and `2/3` that the car is behind other doors. The Monty's choice to open a door (one not chosen by contestant) is not independent of the choice made by the contestant.

So in this case switching doubles the odds of winning.

#### Simulation

Simulating this problem in Python

```Python
def montyChoose(guessDoor, prizeDoor):
    if 1 != guessDoor and 1 != prizeDoor:
        return 1
    if 2 != guessDoor and 2 != prizeDoor:
        return 2
    return 3

def randomChoose(guessDoor, prizeDoor):
    if guessDoor == 1:
        return random.choice([2,3])
    if guessDoor == 2:
        return random.choice([1,3])
    return random.choice([1,2])
    
def simMontyHall(numTrials = 100, chooseFcn = montyChoose):
    stickWins = 0
    switchWins = 0
    noWin = 0
    prizeDoorChoices = [1, 2, 3]
    guessChoices = [1, 2, 3]
    for t in range(numTrials):
        prizeDoor = random.choice([1, 2, 3])
        guess = random.choice([1, 2, 3])
        toOpen = chooseFcn(guess, prizeDoor)
        if toOpen == prizeDoor:
            noWin += 1
        elif guess == prizeDoor:
            stickWins += 1
        else:
            switchWins += 1
    return (stickWins, switchWins)
```

After running a Monte Carlo simulation, we get the following result:

![monty hall](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/monty-hall.png)

These simulations are very useful in solving problems in which predictive non-determinism plays a role.

### Using randomization to solve non-random problems

`Pi = 3.14...` - it has been around for a long time. There have been many estimates of `Pi` over the years in the past. The best estimate in ancient time was made by Archimedes, he gave upper and lower bounds. He concluded that: `223/71 < Pi < 22/7`.

Using a stochasting simulation, you can approximate `Pi`. Inscribing a circle inside a square and then throwing needles inside the square, you can then take number of needles in the circle and the number of needles in the square. Thus needles in circle/needles in square = area circle/area square.

Today with computers and algorithms we can do that much more easily.

```Python
def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def throwNeedles(numNeedles):
    inCircle = 0
    estimates = []
    for Needles in xrange(1, numNeedles + 1, 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1.0:
            inCircle += 1
    return 4*(inCircle/float(Needles))

def estPi(precision = 0.01, numTrials = 20):
    numNeedles = 1000
    numTrials = 20
    sDev = precision
    while sDev >= (precision/4.0):
        estimates = []
        for t in range(numTrials):
            piGuess = throwNeedles(numNeedles)
            estimates.append(piGuess)
        sDev = stdDev(estimates)
        curEst = sum(estimates)/len(estimates) 
        curEst = sum(estimates)/len(estimates)
        print 'Est. = ' + str(curEst) +\
              ', Std. dev. = ' + str(sDev)\
              + ', Needles = ' + str(numNeedles)
        numNeedles *= 2
    return curEst
```

Using `5%` for standard deviation. Running a bigger and bigger trial I can have confidence in my result. Using standard deviation we can tell `Pi` is Est. = 3.14123554688 within standard deviation of 0.00153578981638 with `95%` confidence.

#### Integration problem

You can solve it also with a Monte Carlo simulation. It is practical in solving double integrals.
