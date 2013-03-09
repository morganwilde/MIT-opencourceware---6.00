Distributions, Monte Carlo, and Regressions
===========================================

### Distributions

So far we have learned these distributions:

1. Normal/Gaussian - it looks like a bell curve, the peak is at the mean and it falls off symetrically. It can be fully specified by the standard deviation and the mean. - `(1/root(2Pi*standard_deviation**2) * e)**(-(x-Mean)**2/2standard_deviation**2)`. Standard deviations are also called `sigma`.
2. Uniform - it looks like a horizontal like - `1/b-a`
3. Exponential - it looks like a downward trend

### Monte Carlo method

What a Monte Carlo method is? It is trying to arrive at a solution by large amounts of random sampling.

Monty hall problem - always switch and by switching you will have a 2/3 chance of winning.

```Python
import random

def choose_door():
    return random.choice([1, 2, 3])
    
def play_monty_hall(num_trials = 1000):
    stay_wins = 0
    switch_wins = 0
    for trial in range(num_trials):
        prize_door = choose_door()
        player_door = choose_door()
        if prize_door == player_door:
            stay_wins += 1
        elif prize_door != player_door:
            switch_wins += 1
            
    print 'Stay wins: ', stay_wins / float(num_trials)
    print 'Switch wins: ', switch_wins / float(num_trials)
```

### Regressions
