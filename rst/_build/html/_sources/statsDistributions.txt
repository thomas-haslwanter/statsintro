.. image:: ..\Images\title_distribution.png
    :height: 100 px

.. Distributions of one Variable
.. =============================

Characterizing a Distribution
-----------------------------

Distribution Center 
~~~~~~~~~~~~~~~~~~~~~

Mean 
^^^^^^

By default, when we talk about the *mean value* we mean the *arithmetic
mean* :math:`\bar{x}`:

.. math:: \bar{x} = \frac{{\sum\limits_{i = 1}^n {{x_i}} }}{n}

Median 
^^^^^^^^

The *median* is that value that comes half-way when the data are ranked
in order. In contrast to the mean, it is not affected by outlying data
points.

Mode 
^^^^^^

The *mode* value is the most frequently occurring value in a
distribution.

Geometric Mean 
^^^^^^^^^^^^^^^^

In some situations the *geometric mean* can be useful to describe the
location of a distribution. It is usually close to the median, and can
be calculated via the arithmetic mean of the log of the values.

Quantifying Variability 
~~~~~~~~~~~~~~~~~~~~~~~~~

Range 
^^^^^^^

This one is fairly easy: it is the difference between the highest and
the lowest data value. The only thing that you have to watch out for:
after you have acquired your data, you have to check for *outliers*,
i.e. data points with a value much higher or lower than the rest of the
data. Often, such points are caused by errors in the selection of the
sample or in the measurement procedure. There are a number of tests to
check for outliers. One of them is to check for data which lie more than
1.5\*\ *inter-quartile-range* (IQR) above or below the first/third
quartile (see below).

Centiles 
^^^^^^^^^^

The *Cumulative distribution function (CDF) * tells you for each value
which percentage of the data has a lower value (Figure [fig:CDF]). The
value below which a given percentage of the values occur is called
*centile* or *percentile*, and corresponds to a value with a specified
cumulative frequency.

For example, when you look for the data range which includes 95% of the
data, you have to find the :math:`2.5^{th}` and the :math:`97.5^{th}`
percentile of your sample distribution.

The 50th percentile is the *median*.

Also important are the *quartiles*, i.e. the 25th and the 75th
percentile. The difference between them is sometimes referred to as
*inter-quartile range (IQR)*.

Median, upper and lower quartile are used for the data display in box
plots.

| |image7|

Standard Deviation and Variance 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *variance* (SD) of a distribution is defined as

.. math:: var = \frac{{\sum\limits_{i = 1}^n {({x_i-\bar{x}})^2} }}{n-1}

Note that we divide by *n-1* rather than the more obvious n: dividing by
:math:`n` gives the variance of the observations around the sample mean,
but we virtually always consider our data as a sample from some larger
population and wish to use the sample data to estimate the variability
in the population. Dividing by :math:`n-1` gives us a better estimate of
the population variance.

The *standard deviation* is simply given by the square root of the
variance:

.. math:: s = \sqrt{var}

In statistics it is often common to denote the population standard
deviation with :math:`\sigma`, and the sample standard deviation with
:math:`s`.

Watch out: in Python, by default the variance is calculated for "n". You
have to set "ddof=1" to obtain the variance for "n-1":

::

        In[19]: data = arange(7,14)

        In[20]: std(data, ddof=0)
        Out[20]: 2.0

        In[21]: std(data, ddof=1)
        Out[21]: 2.1602468994692865

Standard Error 
^^^^^^^^^^^^^^^^

While the standard deviation is a good measure for the distribution of
your values, often you are more interested in the distribution of the
mean value. For example, when you measure the response to a new
medication, you might be interested in how well you can characterize
this response, i.e. is how well you know the mean value. This measure is
called the *standard error of the mean*, or sometimes just the *standard
error*. In a single sample from a population with a standard deviation
of :math:`\sigma` the variance of the sampling distribution of the mean
is :math:`\sigma^2/n`, and so the standard error of the mean is
:math:`\sigma/\sqrt{n}`.

Skewness 
^^^^^^^^^^

Distributions are *skewed* if they depart from symmetry. For example, if
you have a measurement that cannot be negative, which is usually the
case, then we can infer that the data have a skewed distribution if the
standard deviation is more than half the mean. Such an asymmetry is
referred to as *positive skewness*. The opposite, negative skewness, is
rare.

Central Limit Theorem 
^^^^^^^^^^^^^^^^^^^^^^^

The central limit theorem states that for identically distributed
independent random variables (also referred to as *random variates*),
the mean of a sufficiently large number of these variables will be
approximately normally distributed.

Distribution Functions
----------------------

The variable for a standardized distribution function is often called
*statistic*. So you often find expressions like "the z-statistic" (for
the normal distribution function), the "t-statistic" (for the
t-distribution) or the "F-statistic" (for the F-distribution).

Probability and Samples
~~~~~~~~~~~~~~~~~~~~~~~

Normal Distribution
~~~~~~~~~~~~~~~~~~~

The *Normal distribution* or *Gaussian distribution* is by far the most
important of all the distribution functions. This is due to the fact
that the mean values of *all* distribution functions approximate a
normal distribution for large enough sample numbers. Mathematically, the
normal distribution is characterized by a mean value :math:`\mu`, and a
standard deviation :math:`\sigma`:

.. math::

   \label{eq_normal}
        f_{\mu,\sigma} (x) = \frac{1}{\sigma \sqrt{2 \pi}} e^{-( x - \mu )^2 /2 \sigma^2}

where :math:` - \infty < x < \infty `, and :math:`f_{\mu,\sigma}` is the
*probability density function (PDF)* .

| |image8|

For smaller sample numbers, the sample distribution can show quite a bit
of variability. For example, look at 25 distributions generated by
sampling 100 numbers from a normal distribution (Fig.
[fig:MultipleNormal])

| |image9|

Some examples of applications are:

-  If the average man is 175 cm tall with a variance of 6 cm, what is
   the probability that a man found at random will be 183 cm tall?

-  If the average man is 175 cm tall with a variance of 6 cm and the
   average woman is 168 cm tall with a variance of 3 cm, what is the
   probability that the average man from a given sample will be shorter
   than the average woman from a given sample?

-  If cans are assumed to have a variance of 4 grams, what does the
   average weight need to be in order to ensure that the 99% of all cans
   have a weight of at least 250 grams?

The normal distribution with parameters :math:`\mu` and :math:`\sigma`
is denoted as :math:`N(\mu,\sigma)`. If the *random variate (rv)* *X* is
normally distributed with expectation :math:`\mu` and standard deviation
:math:`\sigma`, one denotes: :math:`\,X \sim N(\mu,\sigma)` or
:math:`\,X \in N(\mu,\sigma)`.

==================== ===================== ======================
Range                Prob. of being within Prob. of being outside 
==================== ===================== ======================
mean :math:`\pm` 1SD 0.683                  0.317
mean :math:`\pm` 2SD 0.954                  0.046
mean :math:`\pm` 3SD 0.9973                 0.0027
==================== ===================== ======================

The Figure below shows a number of functions are
commonly used to select appropriate points from the normal distribution
function:

-  *Probability density function (PDF)*: note that to obtain the
   probability for the variable appearing in a certain interval, you
   have to *integrate* the PDF over that range.

-  *Cumulative distribution function (CDF)*: gives the probability of
   obtaining a value smaller than the given value

-  *Survival function (SF)*: 1-CDF

-  *Percentile point function (PPF)*: the inverse of the CDF. Answers
   the question "Given a certain probability, what is the corresponding
   value for the CDF?"

-  *Inverse survival function (ISF)*: the name says it all.

| |image10|

Other Continuous Distributions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

t Distribution
^^^^^^^^^^^^^^

For a small number of samples (ca.:math:`<10`) from a normal
distribution, the distribution of the mean deviates slightly from the
normal distribution. The reason is that the sample mean does not
coincide exactly with the population mean. This modified distribution is
the *t-distribution*, and converges for larger values towards the normal
distribution (Fig. [fig:t]).

| |image11|

Chi-square Distribution
^^^^^^^^^^^^^^^^^^^^^^^

The *Chi-square distribution* is related to normal distribution in a
simple way: If a random variable :math:`X` has a normal distribution
(:math:`X \in N(0,1)`), then :math:`X^2` has a chi-square distribution,
with one degree of freedom (:math:`X^2 \in \chi_{1}^2`). The sum squares
of :math:`n` independent and standard normal random variables has a
chi-square distribution with :math:`n` degrees of freedom:

.. math:: \sum\limits_{i = 1}^n {X_i^2} \in \chi_{n}^2

| |image12|

F Distribution
^^^^^^^^^^^^^^

Named after Sir Ronald Fisher, who developed the F distribution for use
in determining critical values in ANOVAs (*ANalysis Of VAriance*). The
cutoff values in an F table are found using three variables:

-  ANOVA numerator degrees of freedom

-  ANOVA denominator degrees of freedom

-  significance level

ANOVA compares the size of the variance between two different samples.
This is done by dividing the larger variance over the smaller variance.
The formula for the resulting *F statistic* is:

.. math:: F(r_1, r_2) = \frac{\chi_{r1} ^2 /r_1}{\chi_{r2} ^2 /r_2}

where :math:`\chi_{r1}^2` and :math:`\chi_{r2}^2` are the chi-square
statistics of sample one and two respectively, and :math:`r_1` and
:math:`r_2` are their degrees of freedom, i.e. the number of
observations.

F-Test of Equality of Variances
'''''''''''''''''''''''''''''''

One example could be if you want to compare apples that look alike but
are from different trees and have different sizes. If you want to
investigate whether they have the same variance of the weight on
average, you have to calculate

.. math:: F = \frac{S_x^2}{S_y^2}

where :math:`S_x` ist he sample standard deviation of the first batch of
apples, and :math:`S_y` the sample standard deviation for the second
batch of apples.

There are three apples from the first tree that weigh 110, 121 and 143
grams respectively, and four from the other which weigh 88, 93, 105 and
124 grams respectively. The F statistic is :math:`F 1.05`, and has
:math:`n-1` and :math:`m-1` degrees of freedom, where :math:`n` and
:math:`m` are the number of apples in each batch. The code sample below
shots what the F statistic is close to the center of the distribution,
so we cannot reject the hypthesis that the two batches have the same
variance.

::

      In [1]:  apples1 = array([110, 121, 143])
      In [2]:  apples2 = array([88, 93, 105, 124])
      In [3]:  fval = std(apples1, ddof=1)/std(apples2, ddof=1)
      In [4]:  fd = stats.distributions.f(3,4)
      In [5]:fd.cdf(fval)
      Out[27]: 0.537640478466751

| |image13|

Lognormal Distribution
^^^^^^^^^^^^^^^^^^^^^^

In some circumstances a set of data with a positively skewed
distribution can be transformed into a symmetric distribution by taking
logarithms. Taking logs of data with a skewed distribution will often
give a distribution that is near to normal (see Figure [fig:lognormal]).

| |image14|

| |image15|
Plotted against a logarithmic abscissa.


Exponential Distribution
^^^^^^^^^^^^^^^^^^^^^^^^

For a stochastic variable X with an *exponential distribution*, the
probability distribution function is:

.. math::

   \label{eq_exponential}
   f_x (x) =
     \begin{cases}
   \lambda e^{- \lambda x}, & \mbox{if } x \ge 0 \\
   0, & \mbox{if } x < 0
   \end{cases}

The exponential PDF is shown in Figure [fig:exponential]

| |image16|

Uniform Distribution
^^^^^^^^^^^^^^^^^^^^

This is a simple one: an even probability for all data values (Figure
[fig:uniform]). Not very common for real data.

| |image17|

Programs: Continuous Distribution Functions 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See also the ipython notebook `dist_continuous.ipynb <http://nbviewer.ipython.org/url/work.thaslwanter.at/CSS/Code/dist_continuous.ipynb>`_:

.. literalinclude:: ..\Code\dist_continuous.py

Discrete Distributions
~~~~~~~~~~~~~~~~~~~~~~

While the functions describing continuous distributions are referred to
as *probability distribution functions*, discrete distributions are
described by *probability mass functions*.

Binomial Distribution
^^^^^^^^^^^^^^^^^^^^^

The Binomial is associated with the question "Out of a given number of
trials, how many will succeed?" Some example questions that are modeled
with a Binomial distribution are:

-  Out of ten tosses, how many times will this coin land ”heads”?

-  From the children born in a given hospital on a given day, how many
   of them will be girls?

-  How many students in a given classroom will have green eyes?

-  How many mosquitos, out of a swarm, will die when sprayed with
   insecticide?

We conduct :math:`n` repeated experiments where the probability of
success is given by the parameter :math:`p` and add up the number of
successes. This number of successes is represented by the random
variable :math:`X`. The value of :math:`X` is then between 0 and
:math:`n`.

When a random variable X has a Binomial Distribution with parameters
:math:`p` and :math:`n` we write it as :math:`\,X \sim Bin(n,p)` or
:math:`\,X \sim B(n,p)` and the probability mass function is given at
:math:`X=k` by the equation:

.. math:: P\left[X = k\right] = \begin{cases} {n \choose k} p^k \left(1-p\right)^{n-k}\ & 0 \le k \le n \\ 0 & \mbox{otherwise} \end{cases} \quad 0 \leq p \leq 1, \quad n \in \mathbb{N}

where :math:`{n \choose k}={n! \over k!(n-k)!}`

| |image18|

Poisson Distribution
^^^^^^^^^^^^^^^^^^^^

Any French speaker will notice that "Poisson" means "fish", but really
there’s nothing fishy about this distribution. It’s actually pretty
straightforward. The name comes from the mathematician Siméon-Denis
Poisson (1781-1840).

The Poisson Distribution is ”very similar” to the Binomial Distribution.
We are examining the number of times an event happens. The difference is
subtle. Whereas the Binomial Distribution looks at how many times we
register a success over a fixed total number of trials, the Poisson
Distribution measures how many times a discrete event occurs, over a
period of continuous space or time. There isn’t a "total" value n. As
with the previous sections, let’s examine a couple of experiments or
questions that might have an underlying Poisson nature.

-  How many pennies will I encounter on my walk home?

-  How many children will be delivered at the hospital today?

-  How many products will I sell after airing a new television
   commercial?

-  How many mosquito bites did you get today after having sprayed with
   insecticide?

-  How many defects will there be per 100 metres of rope sold?

What’s a little different about this distribution is that the random
variable :math:`X` which counts the number of events can take on *any
non-negative integer* value. In other words, I could walk home and find
no pennies on the street. I could also find one penny. It’s also
possible (although unlikely, short of an armored-car exploding nearby)
that I would find 10 or 100 or 10,000 pennies.

Instead of having a parameter p that represents a component probability
like in the Binomial distribution, this time we have the parameter
"lambda" or :math:`\lambda` which represents the "average or expected"
number of events to happen within our experiment. The probability mass
function of the Poisson is given by

.. math:: P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!}

.

| |image19|

Programs: Discrete Distribution Functions 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
See also the ipython notebook `dist_discrete.ipynb <http://nbviewer.ipython.org/url/work.thaslwanter.at/Stats/ipynb/dist_discrete.ipynb>`_:

.. literalinclude:: ..\Code\dist_discrete.py

Data Analysis
-------------

Data Screening
~~~~~~~~~~~~~~

The first thing you have to do for your data analysis is simply *look at
your data*. You should check for *missing data* in your data set, and
*outliers* which can significantly influence the result of your
analysis.

Normality Check
~~~~~~~~~~~~~~~

The first way to check if your data are normally distributed, i.e. that
they are linearly related to the standard normal distribution. In
statistics, *:math:`Q–Q` plots* ("Q" stands for quantile) are used for
visual assessments of distributions. They are a graphical method for
comparing two probability distributions by plotting their quantiles
against each other. First, the set of intervals for the quantiles are
chosen. A point :math:`(x,y)` on the plot corresponds to one of the
quantiles of the second distribution (y-coordinate) plotted against the
same quantile of the first distribution (x-coordinate). Thus the line is
a parametric curve with the parameter which is the (number of the)
interval for the quantile.

If the two distributions being compared are similar, the points in the
:math:`Q-Q` plot will approximately lie on the line :math:`y = x`. If
the distributions are linearly related, the points in the :math:`Q-Q`
plot will approximately lie on a line, but not necessarily on the line
:math:`y = x` (Figure [fig:qqplot]).

| |image20|
QQ-plot

In addition, there are quantitative tests for normality. The test that I
have encountered most frequently in recent literature is the
*Kolmogorov-Smirnov test*.  [1]_ Altman mainly uses the *Shapiro-Wilk W
test* , and a number of other tests are also available.

Transformation
~~~~~~~~~~~~~~

If your data deviate significantly from a normal distribution, it is
sometimes possible to make the distribution approximately normal by
transforming your data. For example, data often have values that can
only be positive (e.g. the size of persons), and that have long positive
tail: such data can often be made normal by applying a *log transform*.
This is demonstrated in Figure [fig:lognormal].

Confidence Intervals
~~~~~~~~~~~~~~~~~~~~

Although it is common to concentrate the analysis on the p-values, it is
often much more informative to report the *confidence intervals* for
your data. The confidence intervals are given by

.. math:: ci = mean \pm se * t_{n,\alpha}

where :math:`se` is the standard error, and :math:`t_{n,\alpha}` the
:math:`t` statistic for :math:`n` degrees of freedom. For the 95%
two-sided confidence intervals, for example, you have to set
:math:`\alpha=0.025` and :math:`\alpha=0.975` .

.. |image7| image:: ../Images/NormalDist_PDF_CDF.png
    :scale: 50 %
.. |image8| image:: ../Images/Normal_Distribution_PDF.png
    :scale: 50 %
.. |image9| image:: ../Images/Normal_MultHist.png
    :scale: 50 %
.. |image10| image:: ../Images/DistributionFunctions.png
    :scale: 75 %
.. |image11| image:: ../Images/Student_t_pdf.png
    :scale: 40 %
.. |image12| image:: ../Images/ChiSquare_pdf.png
    :scale: 40 %
.. |image13| image:: ../Images/F_distributionPDF.png
    :scale: 40 %
.. |image14| image:: ../Images/LogNormal_Linear.png
    :scale: 40 %
.. |image15| image:: ../Images/LogNormal_Logarithmic.png
    :scale: 40 %
.. |image16| image:: ../Images/Exponential_pdf.png
    :scale: 40 %
.. |image17| image:: ../Images/Uniform_Distribution_PDF.png
    :scale: 40 %
.. |image18| image:: ../Images/Binomial_distribution_pmf.png
    :scale: 40 %
.. |image19| image:: ../Images/Poisson_pmf.png
    :scale: 40 %
.. |image20| image:: ../Images/ProbPlot.png
    :scale: 50 %

