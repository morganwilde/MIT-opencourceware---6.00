Some Basic Probability and Plotting Data
========================================

Last lecture result was not credible as in our test results did not match with the ones we got modeling manually.

When the code is fixed, we can begin to see what we can expect from this model. And the best way to see that in this case is by graphin/visualising the data.

After each test we are getting different data.

### How do we think about the results of a program when they are stochastic

In real life situation stochastic results are almost always the case.

#### The role of randomness in computation

Everything in school physics was very comforting, we had a deterministic world. Then came along the **Copenhagen doctrine**. What it argued was that at its most basic, nothing in the physical world is deterministic, rather probabilistic. The world is all stochastic.

The heart of the debate was - **causal non-determinism**. Was the belief that each event was not caused by a previous event. The Copenhagen doctrine argued for **predictive non-determinism**. Our ability to measure the physical world does not determine the outcome deterministically.

We have to assume the world is *non-deterministic*, since we don't know enough to determine that.

### Stochastic processes

A process is stochastic if its next state depends both on its previous state and some random element.

Most programming languages include simple ways to write programs that are random. In the `drunksWalk()` function we already used randomness.

That and almost all other function in Python use `random.random()` to produce a random number.

#### `RollDie()`

```Python
def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])

def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print result
```

Both values:

* 1111111111
* 5442462412

Are equally likely, because each roll is independent of previous rolls. Independence is a very important assumption. The events are independent is the outcome of one event has not influence of another.

In the case of a coin and `10` throws, there are `2**10` possible outcomes and each one is exactly the same. So the probability of any one combination is `1/2**10`.

So the question we're asking is - what fraction of the possible results have property we ask for. Probabilities always will be fractions, they have to be between `0` and `1`.

The probability of not getting all `1` is `1 - 1/2**10`. This would compute the probability of a sequence of all `1` NOT happening.

##### In the case of the die

We have `6**10` different possibilities.

### Visualising data

Many people when are writing code, focus on the problem and what will it return. They don't focus enough on how that data will be presented. This is to allow us to understand the data better.

We don't do it enough is that it is hard in most programming languages. But Python is different because it has the `pylab` module, it provides a lot of the features of `MATLAB`.

In this course the main focus of `pylab` will be **plotting**. [http://matplotlib.org/](http://matplotlib.org/) has all the instructions for that library.

```Python
import pylab

pylab.plot([1,2,3,4], [1,2,3,4]) # key is to plot these when they are of equal length
pylab.plot([1,4,2,3], [5,6,7,8])
pylab.show()
```

This produces the graph below:

![pylab](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/plotting-data.png)

`pylab.show()` - displays the plot on screen. Once per program and that should be the last thing being executed.
