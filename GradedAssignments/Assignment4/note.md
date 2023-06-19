This is the same description as the one at the bottom of Adaline.ipynb...


# Assignment Sketch

### The dataset

We will use the [amphibians](https://archive.ics.uci.edu/ml/datasets/Amphibians) dataset from the UCI ML Repo.

The data needs some preprocessing, such as the following.

1. Drop the ID column
2. Convert the Motorway column to an integer. Replace **A1** with 1 and **S52** with 0.
3. Select one of the frog or toad columns to be the target and copy it into `y` (for example "tree frog"). Replace 0 with -1 so that the classes are $\pm 1$.
4. Copy all the columns that are not frog or toad columns into `X`.
5. Scale the data `X` using Z-score scaling or min-max scaling (your choice).
6. Add a bias column to `X`.

Now you have `X` and `y` and you are ready to do some ML using Adeline.

First try the implementation of Adeline from class on the data and see what kind of accuracy you can get (try tuning $\eta$ a bit and plotting the error curves).

Then it is time for you to write some code...

### Specifications

In class we implemented "vanilla" Adeline.  We used batch gradient descent.

Using this code as a base, implement

1. Adeline using stochastic gradient descent
2. Adeline using mini-batch gradient descent with batches of size 32. 

You can do this by implementing a `fit_adeline_sgd` function (that obviously uses SGD to find `w`) and a `fit_adeline_mbsgd` function that uses mini-batch SGD.  For the latter add `batch_size` as a parameter and give it a default value of 32.

For each approach, plot something like the figure above titled "**Error metric $J(w)$**".

When that works add another twist: shuffling `X` and `y` between epochs.  Note that you need to give `X` and `y` the same shuffle so that the rows correspond after shuffling. 

Does that speed up convergence?

What about trying three different versions of $\eta$?

Try $\eta=0.1$, $\eta=0.01$ and $\eta=0.001$.

Try plotting the error curves for the three versions of $\eta$ all in the same plot.

If you have time see if you can improve SGD performance by using an adaptive learning rate that deceases over time (as described in the book).

If $t$ is the number of iterations, the formula for an adaptive learning rate is

$$\eta(t) = \frac{c_1}{t+c_2}$$

where $c_1$ and $c_2$ are constants that you determine experimentally.  I have no idea what they should be.  Perhaps try $c_1 = c_2 = 1$ as a first guess.

Tuning constants like $c_1$ and $c_2$ is an example of "fitting hyperparameters".  A "hyperparameter" is a parameter of an ML model that is not "fit" during the learning process. The weight vector `w` is a regular parameter because it gets trained automatically.  But for hyperparameters like $c_1$ and $c_2$ you often need to experimentally grope around a bit.





