More Optimization and Clustering
================================

### Greedy algorithms

Last lecture we ended with solving the knapsack problems and the greedy algorithms.

After that we looked at a brute force algorithms, but observed that it would take to long to run to completion.

Generating binary numbers

```Python
def dToB(n, numDigits):
    """requires: n is a natural number less than 2**numDigits
      returns a binary string of length numDigits representing the
              the decimal number n."""
    assert type(n)==int and type(numDigits)==int and\
           n >=0 and n < 2**numDigits
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n//2
    while numDigits - len(bStr) > 0:
        bStr = '0' + bStr
    return bStr
```

This function generates a power set:

```Python
def genPset(Items):
    """Generate a list of lists representing the power set of Items"""
    numSubsets = 2**len(Items)
    templates = []
    for i in range(numSubsets):
        templates.append(dToB(i, len(Items)))
    pset = []
    for t in templates:
        elem = []
        for j in range(len(t)):
            if t[j] == '1':
                elem.append(Items[j])
        pset.append(elem)
    return pset
```

It will generate all the possible sets of all possible items one might takes, irrespective of the constraint that they might weigh too much.

The following function will choose the best set

```Python
def chooseBest(pset, constraint, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for Items in pset:
        ItemsVal = 0.0
        ItemsWeight = 0.0
        for item in Items:
            ItemsVal += getVal(item)
            ItemsWeight += getWeight(item)
        if ItemsWeight <= constraint and ItemsVal > bestVal:
            bestVal = ItemsVal
            bestSet = Items
    return (bestSet, bestVal)
```

This does find a better answer than the greedy algorithm, because the greedy algorithm found only the locally optimal item, not looking at the globally optimal set.

The problem with globally optimal is that is very expensive to run it and that is because brute force is a stupid algorithm. This problem is called inherently exponential. In addition to talking about the complexity of an algorithm, we can also talk about the complexity of a problem.

### Machine learning

Machine learning (ML onwards) is hard to define, but you can say it deals with the question how to build programs that learn. But you can say this about most algorithms. Wikipedia defines it as - a branch of artificial intelligence, is about the construction and study of systems that can learn from data.

A major focus of ML research is to automatically learn to recognize complex patterns and make intelligent decisions based on data, knows as **inductive inference**.

The basic idea is that a program observes examples that represent incomplete information about some statistical phenomenon and tries to generate a model that summarises some statistical properties of that data and cane be used to predict the future. There are two distinctive approaches to machine learning:

1. Supervised learning
    - In supervised learning we associate a label with each example in a training set. If the label is discreet we call it a classification problem. If the labels are real valued we think of it as a regression problem.
2. Unsupervised learning

#### Suppervised learning

![slide 1](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/lect-19-slide-1.png)

So say the data we have are the coordinates of each circle, and their colors are the labels. What can we learn from the labels?

First question I need to ask is:

1. Are the labels accurate? (In most real world examples there is no guarantee that they're accurate)
2. Is the past representative of the future? (Many examples of good learning in the house price industry, but then you hit a singularity and this no longer holds true)
3. Do we have enough data to generalize? (If the data set is small you shouldn't have a lot of confidence)
4. Feature extraction? (The world is pretty complex and we need to decide which features to extract)
5. How tight should the fit be?

There are two ways to classify the data, I.e. devide it.

![slide 2](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/lect-19-slide-2.png)

We might choose this shape and say it's great, why is it great? It minimizes training error. This shape has not training error. If instead we choose the line instead of the triangle, we would have training error. But the triangle would be overfitting to the training data, it might not generalize well.

#### Unsupervised learning

The main difference is that we have training data, but we don't have labels. What can I learn then?

![slide 3](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/lect-19-slide-3.png)

Typically it's learning about regularities of the data. The idea of unsupervised learning is to discover the data **structure**, I.e. finding the **cluster** in this data.

What does clustering mean? It's the process of organizing objects into groups whose members are similar in some way. What do we mean by similar? In this case we can choose between "height", "weight" or a ratio "heigh/weight".

Clustering algorithms are used often, for example in marketing they are used to group customers with similar behaviour. Amazon uses clustering to suggest similar books by assigning visitors to clusters of other users with similar book reading patterns. The insurance industry clusters drivers based on their chances of having an accident.

We can define it as an optimisation problem. What properties a good cluster should have?

1. Low intra-cluster dissimilarity (good cluster all points should be similar)
2. High inter-cluster dissimilarity
    - both can be grouped into badness/goodness of cluster

How might we model dissimilarity? Using variance.

`Variance(Cluster) = sum(X in Cluster) (mean(cluster) - x)**2`

We can use that to talk on how similar the objects in a cluster are or how dissimilar objects in different clusters are.

Is the optimisation problem we're solving in clustering finding the set of clusters `C` such that the badness is minimized? That has the problem of putting each object into its own cluster. We need to add some constraint that will prevent us from finding a trivial solution.

Constraint examples:

1. Maximum number of clusters
2. Maximum distance between two clusters

In general solving this optimization problem is computationally prohibitive. So people usually choose a greedy algorithm to solve them. Examples of such would be:

1. k-means - I want `k` clusters, find the best `k` clustering
2. hierarchical clustering

Both are simple to understand and widely used in practice.

#### hierarchical clustering

We have a set of `n` items to be clustered and a `n*n` distance matrix that tells how far each cluster, example:

![slide 4](http://dl.dropbox.com/u/31042440/mit-ocw-600/unit-2/lect-19-slide-4.png)

How would **hierarchical clustering** relate these things together. We start by:

1. Assigning each item to its own cluster (now we have `n` clusters)
2. Find the most similar pair of clusters and merge them
3. Continue process

So in this example we would merge `New York` and `Boston`. This kind of clustering is called agglomerative. The complication is in step `2`, because we have to define what it means "most similar clusters". It's obvious what to do when having one element, not so much when having multiple elements. The method to do that is using **linkage criterion**:

1. Single-linkage - shortest distance between any pair
2. Complete-linkage - consider between any two clusters by considering the points that are furthest from each other.
3. Average-linkage - take all of the distances and take the average or the median.

The last step from the slide, we have merged everything together. One weakness of this method is that it doesn't scale well, at least `O(n**2)`. And it doesn't neccesarily finds the best solution.

What defined clustering these cities, was choosing the features.

Typically we need to do (dealing with multi-dimensional data) - construct a **feature vector**. So for exmaple for each city we could have `<gps, population>` as a feature vector. How do I compare feature vectors?
