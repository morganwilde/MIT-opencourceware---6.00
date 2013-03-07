Statistical Thinking
====================

Last lecture ended with the question - how can we know that the average result of some finite number of coin flips produces an accurate result?

If we throw it 2 times, we might get heads and tails and conclude that the probability of getting heads is 0.5. This would be correct, but the method of getting to that conclusion would be completely faulty.

### How many samples do we need to have confidence in the result?

The notion of variance. Variance - measure of how much spread there is in the possible outcomes. To be able to have variance, we need to have different outcomes. For that reason we need multiple trials.

If we run 10 trials, and the difference between is vast, we shouldn't use that result.

#### Standard deviation

It is measuring the fraction of values that is close to the mean. If many values are far from the mean, the standard deviation is large. If they are all the same - it is zero.

`StandardDeviation(x) = math.sqrt(1/abs(x) * sum(x)(x - mean)**2)`

This implemented in Python:

```Python
def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5
```

We're going to use it to look at the relationship between the number of samples we have and how much confidence we should have in the answer.

##### Plotting coin flips

First the mean bounces a bit, but then settles around 1

![mean](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/mean-heads-tails-ratios.png)

With more flips, the variance is getting smaller. The results are credible because of a small variance.

![standard deviation](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/standard-deviation-heads-tails-ratios.png)

We expect the difference to get bigger

![mean absolute](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/mean-absolute-heads-tails.png)

The more coins I flip, the bigger the standard deviation is. The key is to compare the standard deviation to the mean.

![standard deviation absolute](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/standard-deviation-absolute-heads-tails.png)

#### Cooefficient of variantion

Standard deviation / mean. This allows us to talk about the relative variance.

If it is `<1` - low variance.

Warnings:

1. If the mean is near zero, small changes in the mean, are going to lead to large changes in the cooefficient of variation
2. Unlike standard deviation, the cooefficient of variantion cannot be used to construct confidence intervals.

#### Example

Now using histograms.

![histogram](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/histogram-example.png)

Comparing flips

![example 1](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/100000-trial-100-flips.png)

![example 2](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/100000-of-1000-flips.png)

The distribution of the results in both cases is close to the **Normal distribution**. It has some interesting properties:

1. Peaks at the mean
2. Falls of symmetrically

Since it looks like a curve, it is called a Bell curve.

But it is not a perfect normal distribution, because it is not symmetric.

### Probabilistic models

Normal distributions are frequently used in contructing probabilistic models for two reasons:

1. Nice mathematical properties (ease to reason about)
2. Many naturally occuring instances

#### Nice mathematically

They can be completely characterized by two parameters:

1. The mean
2. Standard deviation

Knowing these is equivalent to knowing the entire distribution. If we have a normal distribution, they can be used to calculate **confidence intervals**.

Instead of estimating an unknown parameter, by using the mean. Conf. interval instead allows us to estimate the unknown parameter by proving the range that is likely to contain the unknown value. And a confidence that the uknown value lies within that range - aka confidence level.

For example: political polls, the candidate is likely to get 52% of the votes +/- 4%. If the confidence level is not provided, usually it is 5%. So in this case 95% of the elections would result in the candidate getting between 48% and 56% of the votes.

Whenever you see that they are assuming normal distributions.

##### Empirical rule

They give us a handy way to calculate confidence intervals.

* 68% of the data is within 1 standard deviations of mean
* 95% within 2 sd of mean
* 99.7% within 3 sd of mean

Estimating the standard deviation. The technique is called the standard error, you can only do that when the errors are normally distributed. This is not a bad assumption.

`P = % sampled, n = sample size` we can say SE (Standard Error) = `((P(100-P)/n))**0.5` ~ 1.58.

#### Natural occurences

The natural distribution is true in many cases in nature. Normal distribution of measurement errors. A gausian distribution. Most of sience assums normal distribution of errors.
