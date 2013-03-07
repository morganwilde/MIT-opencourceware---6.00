Probability and Statistics
==========================

### Probability

Probability of a binary variables (it can take only two outcomes/two values), examples: 0/1, Heads/Tails, on/off.

`P(A=Heads)` or `P(A=Tails)`, so probability is a way of expresing a belief of something happening. In this case A has only two possible outcomes, but `P(A=Heads)` is anywhere between 0 <= P(A=Heads) <= 1, this range is continous.

`P(A)` = `[0, 1]`

`P(A')` = 1 - `P(A)` - the probability of something not happening.

#### Joint probabilities

| A | B |
|---|---|
| H | T |
| T | H |
| T | T |
| H | H |

Each on of those outcomes has a probability of `1/4`. When measuring joint probabilities we use `P(A = H and B = T)` = `P(A)*P(B)`. This is possible because both events are independent. We call this `P(A intersect B)`.

The case where either A or B gets Tails - `P(A = H or B = H)` = `P(A = H and B = H) * P(A = H and B = T) * P(A = T and B = H)`. We call this `P(A union B)`.

Looking at multiple events:

1. Trees
2. Grid

Probability is the ratio of outcomes and all possible outcomes.

Throwing three coins. There are 8 possible outcomes. Each outcome has a probability of 1/8.

Rolling two four-sided dice, how many possible outcomes are there? Rolling 2 and 3 has 1/16+1/16=1/8 probability of rolling.

What is the probability of getting at least one 4? 1/2 - 1/16

#### Pack of cards

What is the probability of getting an Ace? 4/52. What is the probability of getting Ace of Hearts? 1/52. Probability of not getting an ace? 1-1/13.

What is the sample size when drawing two cards from two different decks? `52*52=2704`

What is the probability of getting at least one Ace?

* first deck - 1/13
* +
* second deck - 1/13
* -
* probability of getting two aces - (1/13)*(1/13)

What is the probability of neither card being an ace? `1 - probability of getting at least one Ace`.

What is the probability of getting two cards of the same suit? 4/16

What is the probability of having neither diamond nor heart? 4/16

#### Summary

Probability is way of expressing a belief of something happening.

### Statistics

#### Simulation

`P = Nheads/Ntrials`. When the probability is unknown we can do a simulation (Monte Carlo in this case) and determine a good enough probability.

The mean of the simulation will give you the expected difference between outcome.

The spread determines what is the variance percent of the standard deviation. The square root of variance is equal to standard deviation.

The way to express the consistence of a distribution - the cooefficient of variance = standard deviation/mean.

Given a normal distribution, within one standard deviation we will have 68% of the values, within two 95% and within three 99.7%.

Suppose you know a probability of something happening, how can we simulate this event? We use the `random.random()` function.
