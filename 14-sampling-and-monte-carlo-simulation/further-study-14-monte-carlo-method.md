Monte Carlo method
==================

Monte Carlo methods are a broad class of computational algorithms that rely on random sampling to obtain numerical results. They are most suited when it is impossible to obtain a closed-form expression/apply a deterministic algorithm.

These are the areas where they're most used:

1. Optimization
2. Numerical integration
3. Generating samples from a probability distribution

They are used to model phenomena with significant uncertainty in input, such as risk calculation in business.

### Introduction

The methods vary, but tend to follow a particular pattern:

1. Define a domain of possible inputs
2. Generate inputs randomly from a probability distribution over the domain
3. Perform a deterministic computation on the inputs
4. Aggregate the results

#### Example

Approximating Pi:

1. Draw a square on the ground, then inscribe a circle within it
2. Uniformly scatter some objects of uniform size over the square
3. Count the number of objects inside the circle and the total number of objects
4. The ratio of the two is the ratio of the two areas - Pi/4. Multiply the result by 4 to estimate Pi

The approcimation improves as more grains are dropped.

### Definitions

**Monte Carlo method** - a technique that can be used to solve a mathematical or statistical problem  
**Monte Carlo simulation** - using repeated sampling to determine the properties of some phenomenon.

#### Examples

* Simulation: drawing **one** pseudo-random variable (0, 1] to simulate a coin toss. This is a simulation, but not a Monte Carlo simulation
* Monte Carlo method: The area of an irregular figure inscribed in a unit square can be determined by throwing darts at the square and computing the ration of hits between the two figures. This is a Monte Carlo method of determining area, not a simulation
* Monte Carlo simulation: drawing **a large number** of pseudo-random variables (0, 1] to simulate a coin toss.

Monte Carlo simulations do not always require truly random numbers to work - pseudo random works also.

Characteristics of a high quality Monte Carlo simulation:

* the (pseudo-random) number generator has certain characteristics (e.g., a long period before the sequence repeats)
* the number generator passes the test for randomness
* there are enough samples to ensure accuracy
* the proper sampling technique is used
* the algorithm used is valid for what is being modeled
* it simulates the phenomenon in question
