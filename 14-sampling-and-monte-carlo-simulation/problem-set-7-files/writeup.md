Problem Set 7 Write-up
======================

### How long it takes for a population to stop growing

After running `1000` tests, the mean amount of steps before the population stops growing is - `53` (with the standard deviation of `3.73614761486`).

Below is a sample illustrating a single simulation of growth:

![single simulation](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/virus-growth-example.png)

Here is the distribution of the number of steps before growth stops:

![growth stops distribution](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/virus-growth-peak-distribution.png)

### Problem 3

#### First part

1. 1/8 - because out of the total possibilities - 8, there is only one combination of 3 heads
2. 1/8 - the same reason
3. 3/8 - out of 8 there are {H, H, T}, {H, T, H}, {T, H, H} - 3 good sequences
4. 1/2 - out of 8 there are {H, H, T}, {H, T, H}, {T, H, H}, {H, H, H} - 4 sequences where it is greater than. No possible sequence has equal amount of tails and heads.

#### Second part

There are `6**5` total possible outcomes of rolling five 6-sided dice. Having them all display 6 only occurs once in all possible rolls, so it is - `1/6**5`
