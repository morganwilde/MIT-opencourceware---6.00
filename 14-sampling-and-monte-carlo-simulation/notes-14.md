Sampling and Monte Carlo Simulation
===================================

### Plotting

Firs example of plotting compound interest:

```Python
import random, pylab

principal = 10000.0 #initial investment
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate
pylab.plot(values)
pylab.show()
```

![plotting](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/plotting-compound-interest.png)

This is a pretty bad example, since it doesn't explain anything about the visual we see. There is not point ever in producing graph without labeling the axis and giving the graph a title. So to fix this we always should use:

```Python
pylab.title('5% Growth, Compounded Annually')
pylab.xlabel('Years of Compounding')
pylab.ylabel('Value of Principal ($)')
pylab.show()
```

![good plotting](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/compound-interest-graph.png)

### Randomness

#### Probability

We have a six-sided die. What is a probability of not rolling a `1` on your first try? `5/6`. Rolling a die 10 times, there are `6**10` possible numbers. How many of those numbers don't contain a `1`. Since each one of those is an independent event, it would be `(5/6)**10`.

What is the probability of getting _at least_ one `1`? `1-(5/6)**10`. Probabilities always have to sum to `1`.

What's the probability of x? Compute the probability of not x, and subtract it from 1.

Probability is closely related with gambling, because all its early developers were interested first by using probability to gain insights into gambling.

Pascal is considered the founder of probability.

##### Pascal problem

Pair of dice. Roll them 24 times. What is the probability of getting `6,6`?

`1/6*1/6 = 1/36` - probability of getting a `6,6` on the first try is this.

`1-1/36 = 35/36` - probability of not getting a `6,6` on the first try

`(35/36)**24 = 0.51` - probability of not getting a `6,6` in ten tries ~ `0.51`.

So there is a slight edge in betting against rolling `6,6` at least once in 24 times.

#### Simulation

We will be doing a lot of that while dealing with probability.

```Python
def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])

def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)

def checkPascal(numTrials = 100000):
    yes = 0.0
    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                yes += 1
                break
    print 'Probability of losing = ' + str(1.0 - yes/numTrials)
```

After running that we get results like these:

```Python
# Probability of losing = 0.50964
# Probability of losing = 0.50795
# Probability of losing = 0.50738
# 
# Calculator probability = 0.50859
```

Is it easier to write a simulation than doing probabilities? In practice doing both is a good thing. This is a good way to test. **You need to have some intuition about the problem**.

#### Monte Carlo simulation

The example above is a type of Monte Carlo simulation, named after a casino. The term was coined in 1949 by Stanislaw Ulam and Nicholas Metropolis.

These simulations are an example of **Inferential Statistics**. In brief it is based on one guiding principle - a random sample tends to exhibit the same properties as the population from which it is drawn.

One always has to ask the question if this is `True`?

Flipping coins. Suppose we flipped it 100 times and we would end up with 52 heads and 48 tails. Would we infer that the probability would skew towards tails? Nope.

Compare something with a NULL hypothesis to an event to see if it is totally random? *Check this later*.

#### Law of Large Numbers

What to look for is a similar answer given a large amount of trials. This is know as the **law of large numbers** aka Bernoulli's law. In repeated independent tests (in this example coin flips) with the same actual probability, `P`, of the outcome for each test, the chance that the fraction of times that outcome occurs converges to `P` as number of trials goes to infinity.

This law does not imply that if we start with a bunch of deviations at the beginning, that we will get an evening out later on. Otherwise these test would not be independent.

`random.random()` is the key function Python has to implement random outcomes.

If you're plotting a small number of points, it is usually better to plot just the points and not connect them with lines. This sometimes saves from mistaking random events having a trend.

Using log scales is extremelly useful too.

How certain can I be?

You can never know you got absolute certainty from sampling. What techniques can I use to be certain that withing a certain range I am correct? Next lecture will deal with that.
