.. image:: ..\Images\title_categorical.png
    :height: 100 px

.. Tests on Categorical Data 
.. ==========================

In a sample of individuals the number falling into a particular group is
called the *frequency*, so the analysis of categorical data is the
analysis of frequencies. When two or more groups are compared the data
are often shown in the form of a *frequency table*, sometimes also
called *contingency table*.



+-------------+------------------+-----------------+-----------+
|             | *Right Handed*   | *Left Handed*   | *Total*   |
+=============+==================+=================+===========+
| *Males*     | 43               | 9               | 52        |
+-------------+------------------+-----------------+-----------+
| *Females*   | 44               | 4               | 48        |
+-------------+------------------+-----------------+-----------+
| *Total*     | 87               | 13              | 100       |
+-------------+------------------+-----------------+-----------+

The corresponding expected values are: 

+-------------+------------------+-----------------+-----------+
|             | *Right Handed*   | *Left Handed*   | *Total*   |
+=============+==================+=================+===========+
| *Males*     | 45.2             | 6.8             | 52        |
+-------------+------------------+-----------------+-----------+
| *Females*   | 41.8             | 6.2             | 48        |
+-------------+------------------+-----------------+-----------+
| *Total*     | 87               | 13              | 100       |
+-------------+------------------+-----------------+-----------+

If you have only one sample group of data, the analysis options are somewhat limited. In contrast, a number of statistical tests exist for the analysis of frequency tables.

Chi-square Test
    This is the most common type. It is a hypothesis test,
    which checks if the entries in the individual cells all come from the same
    distribution. In other words, it checks the null hypothesis *H_0* that the
    results are independent of the row or column in which they appear. The
    alternative hypothesis *H_a* does not specify the type of association, so
    close attention to the data is required to interpret the information
    provided by the test.


Fisher's Exact Test
    While the chi-square test is approximate, the *Fisher's Exact Test* is an exact test. As it is computationally much more expensive and intricate than the chi-square test, it was originally used only for small sample numbers. However, in general it is now the more advisable test to use.

McNemar's Test
    This is a matched pair test for 2x2 tables.

Cochran's Q Test
    Cochran's Q test is an extension to the McNemar's test for related samples that provides a method for testing for differences between three or more *matched/paired* sets of frequencies or proportions. For example, if you have exactly the same samples analyzed by 3 different laboratories, and you want to check if the results are statistically equivalent, you would use this test.

One Proportion 
---------------

If you have one sample group of data, you can check if your sample is
representative of the standard population. To do so, you have to know
the proportion :math:`p` of the characteristic in the standard
population. It can be shown that a in population with a characteristic
with probability :math:`p`, the standard error of samples with this
characteristic is given by

.. math:: se(p) = \sqrt{p(1-p)/n}

and the corresponding 95% confidence interval is

.. math:: ci = mean \pm se * t_{n,0.95}

If your data lie outside this confidence interval, they are *not*
representative of the population.

Frequency Tables
----------------

Chi-square Test
~~~~~~~~~~~~~~~

The chi-square test is based on a test statistic that measures the
divergence of the observed data from the values that would be expected
under the null hypothesis of no association. This requires calculation
of the expected values based on the data.
With *n* is the total number of observations included in the table,
the expected value :math:`e_i`` for each cell in a two-way table is

.. math::
    
    expected = \frac{row total*column total}{n}

Assume you have observed absolute frequencies :math:`o_i` and expected
absolute frequencies :math:`e_i` under the Null hypothesis of your test
then it holds

.. math:: V = \sum_i \frac{(o_i-e_i)^2}{e_i} \approx \chi^2_f

.

where :math:`f` are the degrees of freedom. :math:`i` might denote a
simple index running from :math:`1,...,I` or even a multiindex
:math:`(i_1,...,i_p)` running from :math:`(1,...,1)` to
:math:`(I_1,...,I_p)`.

Assumptions
^^^^^^^^^^^^

The test statistic :math:`V` is approximately :math:`\chi^2`
distributed, if

-  for all absolute expected frequencies :math:`e_i` holds
   :math:`e_i \geq 1` and

-  for at least 80% of the absolute expected frequencies :math:`e_i`
   holds :math:`e_i \geq 5`.

For small sample numbers, corrections should be made for some bias that
is caused by the use of the continuous chi-squared distribution. This
correction is referred to as *Yates correction*.

Degrees of Freedom
^^^^^^^^^^^^^^^^^^

The degrees of freedom can be computed by the numbers of absolute observed
frequencies which can be chosen freely. For example, only one cell of a 2x2 table
with the sums at the side and bottom needs to be filled, and the others can be
found by subtraction. In general, an *r x c* table has *df=(r-1)x(c-1)*
degrees of freedom. We know that the sum of absolute expected frequencies is

.. math:: \sum_i o_i = n

which means that the maximum number of degrees of freedom is
:math:`I-1`. We might have to subtract from the number of degrees of
freedom the number of parameters we need to estimate from the sample,
since this implies further relationships between the observed
frequencies.

Example 1
^^^^^^^^^

The Python command *stats.chi2_contingency* returns, the chi2-value, the p-value, the degrees of freedom, and the expected values. For the example data in Table above, the results are *\chi^2=1.1, p=0.3, df=1*. In other words, there is no indication that there is a difference in left-handed people vs right-handed people between males and females.

Example 2
^^^^^^^^^

The :math:`\chi^2` test can be used to generate "quick and dirty" test,
e.g.

:math:`H_0:` The random variable :math:`X` is symmetrically distributed
versus

:math:`H_1:` the random variable :math:`X` is not symmetrically
distributed.

We know that in case of a symmetrical distribution the arithmetic mean
:math:`\bar{x}` and median should be nearly the same. So a simple way to
test this hypothesis would be to count how many observations are less
than the mean (:math:`n_-`)and how many observations are larger than the
arithmetic mean (:math:`n_+`). If mean and median are the same than 50%
of the observation should smaller than the mean and 50% should be larger
than the mean. It holds

.. math:: V = \frac{(n_- - n/2)^2}{n/2} + \frac{(n_+ - n/2)^2}{n/2} \approx \chi^2_1

.

Comments
^^^^^^^^

The Chi-square test is a pure hypothesis test. It tells you if your
observed frequency can be due to a random sample selection from a single
population. A number of different expressions have been used for
chi-square tests, which are due to the original derivation of the
formulas (from the time before computers were pervasive). Expression
such as *2x2 tables*, *r-c tables*, or *Chi-square test of contingency*
all refer to frequency tables and are typically analyzed with chi-square
tests.

Fisher's Exact Test
~~~~~~~~~~~~~~~~~~~

If the requirement that 80% of cells should have expected values of at least
5 is not fulfilled, *Fisher's exact test* should be used. This test is based
on the observed row and column totals. The method consists of evaluating the
probability associated with all possible 2x2 tables which have the same row
and column totals as the observed data, making the assumption that the null
hypothesis (i.e. that the row and column variables are unrelated) is true.
In most cases, Fisher's exact test is preferable to the chi-square test. But
until the advent of powerful computers, it was not practical. You should use
it up to approximately 10-15 cells in the frequency tables. It is called
"exact" because the significance of the deviation from a null hypothesis can
be calculated exactly, rather than relying on an approximation that becomes
exact in the limit as the sample size grows to infinity, as with many
statistical tests.

Fisher is said to have devised the test following a comment from Dr Muriel
Bristol, who claimed to be able to detect whether the tea or the milk was
added first to her cup. The test is useful for categorical data that result
from classifying objects in two different ways; it is used to examine the
significance of the association (contingency) between the two kinds of
classification. So in Fisher's original example, one criterion of
classification could be whether milk or tea was put in the cup first; the
other could be whether Dr Bristol thinks that the milk or tea was put in
first. We want to know whether these two classifications are associated -
that is, whether Dr Bristol really can tell whether milk or tea was poured
in first. Most uses of the Fisher test involve, like this example, a 2 x 2
contingency table. The p-value from the test is computed as if the margins
of the table are fixed, i.e. as if, in the tea-tasting example, Dr Bristol
knows the number of cups with each treatment (milk or tea first) and will
therefore provide guesses with the correct number in each category. As
pointed out by Fisher, this leads under a null hypothesis of independence to
a hypergeometric distribution of the numbers in the cells of the table.

In using the test, you have to decide if you want to use a one-tailed test
or a two-tailed test. The former one looks for the probability to find a
distribution as extreme or more extreme as the observed one. The latter one
(which is the default in python) also considers tables as extreme in the
opposite direction.


+--------+-------+-------+-----------+
|        | B     | B     |           |
|        | 1     | 0     | *Totals*  |
+========+=======+=======+===========+
| A   1  | a     | b     | a+b       |
+--------+-------+-------+-----------+
| A   0  | c     | d     | c+d       |
+--------+-------+-------+-----------+
| Totals | a+c   | b+d   | a+b+c+d=N |
+--------+-------+-------+-----------+

*General Structure of 2x2 Frequency Tables*

McNemar's Test
~~~~~~~~~~~~~~

Although the McNemar test bears a superficial resemblance to a test of
categorical association, as might be performed by a 2x2 chi-square test or
a 2x2 Fisher exact probability test, it is doing something quite different.
The test of association examines the relationship that exists among the
cells of the table. The McNemar test examines the difference between the
proportions that derive from the marginal sums of the table (see Table):
:math:`p_A=(a+b)/N` and :math:`p_B=(a+c)/N`. The question in the McNemar
test is: do these two proportions, :math:`p_A` and :math:`p_B`,
significantly differ? And the answer it receives must take into account the
fact that the two proportions are not independent. The correlation of
:math:`p_A` and :math:`p_B` is occasioned by the fact that both include the
quantity a in the upper left cell of the table.

Example
^^^^^^^

In the following example, a researcher attempts to determine if a drug has an effect on a particular disease. Counts of individuals are given in the table, with the diagnosis (disease: present or absent) before treatment given in the rows, and the diagnosis after treatment in the columns. The test requires the same subjects to be included in the before-and-after measurements (matched pairs).

+-----------------+------------------+-----------------+-----------+
|                 | After: present   | After: absent   | Row total |
+=================+==================+=================+===========+
| Before: present | 101              | 121             | 222       |
+-----------------+------------------+-----------------+-----------+
| Before: absent  |  59              |  33             |  92       |
+-----------------+------------------+-----------------+-----------+
| Column total    | 160              | 154             | 314       |
+-----------------+------------------+-----------------+-----------+

*McNemar's Test: example*


In this example, the null hypothesis of "marginal homogeneity" would mean there
was no effect of the treatment. From the above data, the McNemar test statistic
with Yates's continuity correction is

The general solution for the McNemar's test is

.. math::    \chi^2 = {(|b-c|-correctionFactor)^2 \over b+c}.

For small number of sample numbers the \emph{correctionFactor} should be 0.5
(*Yates's correction*) or 1.0 (*Edward's correction*). (In fact, for
small numbers an exact calculation is typically done for the probabilities, based
on a binomial test.) Using Yates's correction, we get

.. math::     \chi^2 = {(|121 - 59| - 0.5)^2 \over {121 + 59}}

has the value 21.01, which is extremely unlikely from the distribution implied by
the null hypothesis. Thus the test provides strong evidence to reject the null
hypothesis of no treatment effect.


Cochran's Q Test
~~~~~~~~~~~~~~~~

Cochran's Q test is a hypothesis test where the response variable can take
only two possible outcomes (coded as 0 and 1). It is a non-parametric
statistical test to verify if k treatments have identical effects. Cochran's
Q test should not be confused with *Cochran's C test*, which is a variance
outlier test.

Example
^^^^^^^

12 subjects are asked to perform 3 tasks. The outcome of each task is
*success* or *failure*. The results are coded *0* for *failure* and *1* for
*success*. In the example, subject 1 was successful in task 2, but failed
tasks 1 and 3 (see Table).


+--------+--------+--------+--------+
| Subject| Task 1 | Task 2 | Task 3 |
+========+========+========+========+
| 1      | 0      | 1      | 0      |
+--------+--------+--------+--------+
| 2      | 1      | 1      | 0      |
+--------+--------+--------+--------+
| 3      | 1      | 1      | 1      |
+--------+--------+--------+--------+
| 4      | 0      | 0      | 0      |
+--------+--------+--------+--------+
| 5      | 1      | 0      | 0      |
+--------+--------+--------+--------+
| 6      | 0      | 1      | 1      |
+--------+--------+--------+--------+
| 7      | 0      | 0      | 0      |
+--------+--------+--------+--------+
| 8      | 1      | 1      | 0      |
+--------+--------+--------+--------+
| 9      | 0      | 1      | 0      |
+--------+--------+--------+--------+
| 10     | 0      | 1      | 0      |
+--------+--------+--------+--------+
| 11     | 0      | 1      | 0      |
+--------+--------+--------+--------+
| 12     | 0      | 1      | 0      |
+--------+--------+--------+--------+

*Cochran's Q Test: Success or failure for 12 subjects on 3 tasks*

The null hypothesis for the Cochran's Q test is that there are no
differences between the variables. If the calculated probability *p* is
below the selected significance level, the null-hypothesis is rejected, and
it can be concluded that the proportions in at least 2 of the variables are
significantly different from each other. For our example, the analysis of
the data provides *Cochran's Q = 8.6667* and a significance of *p = 0.013*.
In other words, at least one of the three Tasks is easier or harder than the
others.

Analysis Programs
-----------------

With computers, the computational steps are trivial
(See also the ipython notebook `compGroups.ipynb <http://nbviewer.ipython.org/url/raw.github.com/thomas-haslwanter/statsintro/master/ipynb/ compGroups.ipynb>`_):

.. literalinclude:: ..\Code3\compGroups.py


Exercises
---------

Fisher's Exact Test - The Tea Experiment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At a party, a lady claimed to be able to tell whether the tea or the
milk was added first to a cup. Fisher proposed to give her eight cups,
four of each variety, in random order. One could then ask what the
probability was for her getting the number she got correct, but just by
chance.

The experiment provided the Lady with 8 randomly ordered cups of tea - 4
prepared by first adding milk, 4 prepared by first adding the tea. She
was to select the 4 cups prepared by one method. (This offered the Lady
the advantage of judging cups by comparison.)

The null hypothesis was that the Lady had no such ability.

Calculate if the claim of the lady is supported if she gets three out of
the four pairs correct. (Correct answer: No. If she gets three correct,
that chance that a selection of "three or greater" was random is 0.243.
She needs to get all four correct, if we set the rejection threshold at
0.05)
