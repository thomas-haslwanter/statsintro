.. image:: ..\Images\title_continuous.png
    :height: 100 px

.. Test of Means of Continuous Data

Distribution of a Sample Mean
-----------------------------

One sample t-test for a mean value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If we knew the mean and the standard deviation of a normally distributed
population, we would know exactly the standard error, and use values
from the normal distribution to determine how likely it is to find a
certain mean value, given the population mean and standard deviation.
However, in practice we have to *estimate* the mean and standard
deviation from the sample, and the resulting distribution for the mean
value deviates slightly from a normal distribution. Such distributions
are called *t-distributions*, and were first described by a researcher
working under the pseudonym of "Student".

Let us look at a specific example: we take 100 normally distributed
data, with a mean of 7 and with a standard deviation of 3. What is the
chance of finding a mean value at a distance of 0.5 or more from the
mean:?

See also the ipython notebook `ttest_1samp_notebook.ipynb <http://nbviewer.ipython.org/url/work.thaslwanter.at/CSS/Code/ttest_1samp_notebook.ipynb>`_:

.. literalinclude:: ..\Code\ttest_1samp_notebook.py

:math:`>>>` The probability from the t-test is 0.057, and from the
normal distribution 0.054

Wilcoxon signed rank sum test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If our data are not normally distributed, we cannot use the t-test
(although this test is fairly robust against deviations from normality).
Instead, we must use a *non-parametric* test on the mean value. We can
do this by performing a *Wilcoxon signed rank sum test*.  [2]_  [3]_
This method has three steps:

#. Calculate the difference between each observation and the value of
   interest.

#. Ignoring the signs of the differences, rank them in order of
   magnitude.

#. Calculate the sum of the ranks of all the negative (or positive)
   ranks, corresponding to the observations below (or above) the chosen
   hypothetical value.

In Table [tab:wilcoxon] you see an example, where the significance to a
deviation from the value of 7725 is tested. The rank sum of the negative
values gives :math:`3+5=8`, and can be looked up in the corresponding
tables to be significant. In practice, your computer program will
nowadays do this for you. This example also shows another feature of
rank evaluations: tied values (here :math:`7515`) get accorded their
mean rank (here :math:`1.5`).

======= ======================== ======================= =====================
Subject Daily energy intake (kJ) Difference from 7725 kJ Ranks of differences
======= ======================== ======================= =====================
 1       5260                    2465                    11
 2       5470                    2255                    10
 3       5640                    2085                    9
 4       6180                    1545                    8
 5       6390                    1335                    7
 6       6515                    1210                    6
 7       6805                    920                     4
 8       7515                    210                     1.5
 9       7515                    210                     1.5
 10      8230                    -505                    3
 11      8770                    -1045                   5
======= ======================== ======================= =====================

Comparison of Two Groups
------------------------

When you compare two groups with each other, we have to distinguish
between two cases. In the first case, we compare two values recorded
from the same subject at two specific times. For example, we measure the
size of students when they enter primary school and after their first
year, and check if they have been growing. Since we are only interested
in the *difference* between the first and the second measurement, this
test is called *paired t-test*, and is essentially equivalent to a
one-sample t-test for the mean difference.

The second test is if we compare two independent groups. For example, we
can compare the effect of a two medications given to two different
groups of patients, and compare how the two groups respond. This is
called an *unpaired t-test*, or *t-test for two independent groups*.

If we have two independent samples the variance of the difference
between their means is the *sum* of the separate variances, so the
standard error of the difference in means is the square root of the sum
of the separate variances:

.. math::

   \begin{aligned}
      se({{\bar x}_1} - {{\bar x}_2}) &= \sqrt {\operatorname{var} ({{\bar x}_1}) + \operatorname{var} ({{\bar x}_2})}  \\
      &= \sqrt {{{\left\{ {se({{\bar x}_1})} \right\}}^2} + {{\left\{ {se({{\bar x}_2})} \right\}}^2}}  \\
      &= \sqrt {\frac{{s_1^2}}{{{n_1}}} + \frac{{s_2^2}}{{{n_2}}}}  \\\end{aligned}

where :math:`\bar{x}_i` is the mean of the i-th sample, and *se*
indicates the *standard error*.

See also the ipython notebook `univariate.ipynb <http://nbviewer.ipython.org/url/work.thaslwanter.at/Stats/ipynb/univariate.ipynb>`_:

.. literalinclude:: ..\Code\univariate.py

Non-parametric Comparison of Two Groups: Mann-Whitney Test 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the measurement values from the two groups are not normally
distributed we have to resort to a non-parametric test. The most common
test for that is the *Mann-Whitney(-Wilkoxon) test*.

Comparison of More Groups
-------------------------

Analysis of Variance 
~~~~~~~~~~~~~~~~~~~~~~

If we want to compare three or more groups with each other, we need to
use a *one way analysis of variance (ANOVA)*, sometimes also called a
*one factor ANOVA*. Because the null hypothesis is that there is no
difference between the groups, the test is based on a comparison of the
observed variation between the groups (i.e. between their means) with
that expected from the observed variability between subjects. The
comparison takes the general form of an *F test* to compare variances,
but for two groups the t test leads to exactly the same answer. We will
discuss ANOVAs in more detail in chapter [sec:anova].

F Test 
^^^^^^^^

The :math:`F` test or *variance ratio test* is very simple. Under the
null hypothesis that two Normally distributed populations have equal
variances we expect the ratio of the two sample variances to have an *F
distribution* (see section [sec:ContinuousDistributions]).

Bonferroni correction 
^^^^^^^^^^^^^^^^^^^^^^^

If an ANOVA yields a significant result, we have to test which of the
groups are different. Typically, this is done with :math:`t-tests`.
Since we perform multiple t tests, we should compensate for the risk of
getting a significant result, even if our null hypothesis is true. The
simplest - and at the same time quite conservative - approach is to
divide the required p-value by the number of tests that we do
(*Bonferroni correction*). For example, if you perform 4 comparisons,
you check for significance not at :math:`p=0.05`, but at
:math:`p=0.0125`.

While multiple testing is not yet included in Python standardly, you can
get a number of multiple-testing corrections done with the statsmodels
package:

::

      In[7]: from statsmodels.sandbox.stats.multicomp import multipletests
      In[8]: multipletests([.05, 0.3, 0.01], method='bonferroni')
      Out[8]:
      (array([False, False,  True], dtype=bool),
      array([ 0.15,  0.9 ,  0.03]),
      0.016952427508441503,
      0.016666666666666666)

Kruskal-Wallis test 
~~~~~~~~~~~~~~~~~~~~~

Just as analysis of variance is a more general form of :math:`t` test,
so there is a more general form of the non-parametric Mann-whitney test:
the *Kruskal-Wallis test*. When the null hypothesis is true the test
statistic follows the *Chi squared distribution*.
See also the ipython notebook `anovat.ipynb <http://nbviewer.ipython.org/url/work.thaslwanter.at/CSS/Code/anovat.ipynb>`_:

.. literalinclude:: ..\Code\anovat.py


.. [2]
   Python Example: scipy.stats.wilcoxon, in "univariate.py"

.. [3]
   The following description and example has been taken from Altman, Table 9.2
