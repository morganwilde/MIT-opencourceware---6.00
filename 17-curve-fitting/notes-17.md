Curve Fitting
=============

Last lecture ended with confusing a statistically sound notion being understood as truth. Every statistical test runs on assumptions and the key assumption was that our model was representative of reality.

Suppose we had made a coding error. The moral is: before believing the results of any simulation we have to have confidence that our conceptual model of reality is correct. How can we do that? Test our results against reality. Always runs experiments that would show whether the model is at least plausible.

**Interplay between physical reality, theoretical models and computational models**

This is how modern science and engineering is done these days.

### Experimental errors

The best way to model experimental errors is to assume some sort of random perturbation of the actual data. This can typically be modeled using a normal distribution.

#### Springs

1676 Rober Hook formulated **Hooks law** - `F = -kx` - the force `F` is linearly related to `x` the distance of spring being stretched. All springs have an elastic limit at which the law no longer holds true. `k` is the spring constant that explains its behaviour, if the spring is stiff, the `k` is large. Knowing `k` is very important practically.

*Lecture slide 1*

![slide 1](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/slide-lec17-1.png)

A method of calculating `k` using a practical experiment. This would be all well and good if we didn't have experimental errors. Therefore if we do enough experiments, we can have a good enough estimate of `k`.

Having collected the experimental data in the file `springData.txt`, we can then plot it:

```Python
def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    discardHeader = dataFile.readline()
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)

def plotData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81  #acc. due to gravity
    pylab.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')
```

In this case we come accross a new data type included in `pylab` and that is an `array` and they have handy attributes, I.e. multiplying all values of adding two arrays and so on.

The plot turns out like this:

![plot](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/measured-displacement-of-spring.png)

Before calculating `k` we have to check if this data is sensible. What we often have a theoretical model, and the model here is that the data should fall on a line (modular experimental errors). We're now going to find what the line is and see how `k` relates to it.

How to get the line? Find a line that is the best approximation to the points I have. When having a lot of scatter points, we have to find the best fit. To do that we need some measure of a good fit, thus we need an objective function that tells me how good is a comparative fit.

There are lots of possibilities. But the standard measure for that is the **least squares fit**. The wikipedia article on this is [here](http://en.wikipedia.org/wiki/Least_squares).

Once we have a fit, for every `x` value the model predicts the `y` value. But in addition to predicted values we have the observed values. So we take the difference between the predicted and the observed, square it, them sum it all up. The smaller we can make that value, the better the fit.

`pylab` has this function already implemented - `polyfit(observedX, observedY, degreeOfThePolynomial)`. A line is defined `y = ax + b`. Here is the implementation of a `fitdata()` function using `polyfit()`

```Python
def fitData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81
    pylab.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')
    a,b = pylab.polyfit(xVals, yVals, 1)
    estYVals = a*pylab.array(xVals) + b
    k = 1/a
    pylab.plot(xVals, estYVals, label = 'Linear fit, k = '
               + str(round(k, 5)))
    pylab.legend(loc = 'best')
```

This plots the following results:

![plot 2](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/linear-fit.png)

This produces `k` as `21.53686`. The method that is used to do this in `pylab` is called a **linear regression**. A parabola is `y = ax**2 + bx + c` and this can also be solved using linear regression.

Just by looking at the fit, it shows large variations above and below the line, which is a reason to get suspicious. If we make the change for a cubic fit, using the following code:

```Python
def fitData2(fileName):
    xVals, yVals = getData(fileName)
    extX = pylab.array(xVals + [1.5])
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81
    extX = extX*9.81
    pylab.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')
    a,b = pylab.polyfit(xVals, yVals, 1)
    extY = a*pylab.array(extX) + b
    pylab.plot(extX, extY, label = 'Linear fit')
    a,b,c,d = pylab.polyfit(xVals, yVals, 3)
    extY = a*(extX**3) + b*extX**2 + c*extX + d
    pylab.plot(extX, extY, label = 'Cubic fit')
    pylab.legend(loc = 'best')
```

We get this plot:

![cubic fit](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/cubic-fit.png)

Which turns out to be a much better fit just by judging the distances of point above and below the fit. This is a much better model of the data than a line. Should we be happy of this?

The question to ask why are we building a model? One reason is to get values we can't get by experimentation, I.e. nuclear tests. In this even though we can fit a model to the data, it does have very bad predictive values.

It turns out that if you have a high enough polynomial in the model, you can fit almost any data to a curve.

It's very important to look at the data first. By looking the plot, we can see an evening out of the data towards the right, but Hooks law tells us that is the relation between distance and force should be linear. Does the data violate Hooks law?

No. Because Hooks law applies only until the limit of elasticity. So what the data tells us is that we probably exceeded the elasticity in our experiments.

Once we remove the last six items from the data, we get a much tighter fit from the linear fit to the data points. How do we know which model is good?

This is a question that can't be answered by statistics. In this case (elastic limit) we can plausibly remove the last six data points, because the theoretical model says it only holds true until the elastic limit, and since after removing the last 6 data points we do get a tight fit, we may argue that they were achieved after exceeding the eslastic limit.

### Bow and arrow

Finding the trajectory of a projectile. Modeling it we get this plot:

![projectile](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/trajectory.png)

The theory of an arrow going straight could be debunked by comparing the linear fit with the data points. A much better fit comes from a quadratic fit. Our eyes tells us that it is a better fit, but by how much? How can we compare them?

We can do that by comparing the mean square error of the line and the mean square error of the parabola. Computing a mean square error is a good way of comparing the fit of two different curves.

However it is not particularly good at telling the goodness of the fit in absolute terms. Why is that so? Because mean square error, has a lower bound - `0`, but there is not upper bound. It can go arbitralily high.

Instead what we typically use is the **cooefficient of determination**. Usually written as `r**2 = 1 - estimated_error/variance_in_measured_data`. What are these values, how do we compute them? In python:

```Python
def rSquare(measured, estimated):
    """measured: one dimensional array of measured values
       estimate: one dimensional array of predicted values"""
    EE = ((estimated - measured)**2).sum()
    mMean = measured.sum()/float(len(measured))
    MV = ((mMean - measured)**2).sum()
    return 1 - EE/MV
```
