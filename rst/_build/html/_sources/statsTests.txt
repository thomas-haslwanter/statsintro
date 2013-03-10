.. image:: ..\Images\title_tests.png
    :height: 100 px

.. Statistical Tests 
.. ===================

Hypothesis tests
----------------

[sec:hypotheses] Statistical evaluations are based on the initially
often counterintuitive procedure of *hypothesis tests*. A hypothesis
test is a standard format for assessing statistical evidence. It is
ubiquitous in scientific literature, most often appearing in the form of
statements of *statistical significance* and quotations like
:math:`"p<0.01"` that pepper scientific journals. Thereby you proceed as
follows: you

-  state your hypothesis.

-  decide which value you want to test your hypothesis on.

-  calculate the *probability p* that you find the given value, assuming
   that your hypothesis is true

The first hypothesis is referred to as *null-hypothesis*, since we
assume that there is *null* difference between the hypothesis and the
result. The found probability for a specific target value is the
*p-value* that you typically find in the literature. If :math:`p<0.05`,
the difference between your sample and the value that you check is
*significant*. If :math:`p<0.001`, we speak of a *highly significant*
difference.

An example for a *null hypothesis*: "We assume that our population has a
mean value of 7."

Types of Error
~~~~~~~~~~~~~~~

In hypothesis testing, two types of errors can occur:

Type I errors
^^^^^^^^^^^^^

These are errors, where you get a significant result despite the fact
that the hypothesis is true. The likelihood of a Type I error is
commonly indicated with :math:`\alpha`, and *is set before you start the
data analysis*.

For example, assume that the population of young Austrian adults has a
mean IQ of 105 (i.e. we are smarter than the rest) and a standard
deviation of 15. We now want to check if the average FH student in Linz
has the same IQ as the average Austrian, and we select 20 students. We
set :math:`\alpha=0.05`, i.e. we set our significance level to 95%. Let
us now assume that the average student has in fact the same IQ as the
average Austrian. If we repeat our study 20 times, we will find one of
those 20 times that our sample mean is significantly different from the
Austrian average IQ. Such a finding would be a false result, despite the
fact that our assumption is correct, and would constitute a *type I
error*.

Type II errors and Test Power
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If we want to answer the question "How much chance do we have to reject
the null hypothesis when the alternative is in fact true?" Or in other
words, "What’s the probability of detecting a real effect?" we are faced
with a different problem. To answer these questions, we need an
*alternative hypothesis*.

For the example given above, an *alternative hypothesis* could be: "We
assume that our population has a mean value of 6."

A *Type II error* is an error, where you do *not* get a significant
result, despite the fact that the null-hypothesis is false. The
probability for this type of error is commonly indicated with
:math:`\beta`. The *power* of a statistical test is defined as
:math:`(1-\beta)*100`, and is the chance of correctly accepting the
alternate hypothesis. Figure [fig:power1] shows the meaning of the
*power* of a statistical test. Note that for finding the power of a
test, you need an alternative hypothesis.

Sample Size
~~~~~~~~~~~

The power of a statistical test depends on four factors:

#. :math:`\alpha`, the probability for Type I errors

#. :math:`\beta`, the probability for Type II errors (
   :math:`\Rightarrow` power of the test)

#. :math:`d`, the magnitude of the investigated effect relative to
   :math:`\sigma`, the standard deviation of the sample

#. :math:`n`, the sample size

Only 3 of these 4 parameters can be chosen, the :math:`4^{th}` is then
automatically fixed.

The size of the difference, :math:`d`, between mean treatment outcomes
that will answer the clinical question being posed is often called
*clinical significance* or *clinical relevance*.

| |image21|

| |image22|

Examples for some special cases 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a test on one mean, this leads to a *minimum sample number* of

.. math:: n = \frac{{{{({z_{1 - \alpha /2}} + {z_{1 - \beta }})}^2}{\sigma ^2}}}{{{d^2}}}

Here z is the standardized normal variable (see also chapter
[sec:normalDistribution])

.. math:: z = \frac{x-\mu}{\sigma} .

For finding a difference between two normally distributed means, the
minimum number of samples we need in each group is

.. math:: {n_1} = {n_2} = \frac{{({z_{1 - \alpha /2}} + {z_{1 - \beta }})}^2(\sigma _1^2 + \sigma _2^2)}{d^2} .

Programs: SampleSize 
^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ..\Code\sampleSize.py

Sensitivity and Specificity 
-----------------------------

Some of the more confusing terms in statistical analysis are
*sensitivity* and *specificity* . A related topic are *positive
predictive value (PPV)* and *negative predictive value (NPV)* . The
following diagram shows how the four are related:

| |image23|

-  **Sensitivity** = proportion of positives that are correctly
   identified by a test = probability of a positive test, given the
   patient is ill.

-  **Specificity** = proportion of negatives that are correctly
   identified by a test = probability of a negative test, given that
   patient is well.

-  **Positive predictive value** is the proportion of patients with
   positive test results who are correctly diagnosed.

-  **Negative predictive value** is the proportion of patients with
   negative test results who are correctly diagnosed.

While sensitivity and specificity are independent of prevalence, they do
not tell us what portion of patients with abnormal test results are
truly abnormal. This information is provided by the positive/negative
predictive value. However, as Fig. [fig:prevalence] indicates, these
values are affected by the *prevalence* of the disease. In other words,
we need to know the prevalence of the disease as well as the PPV/NPV of
a test to provide a sensible interpretation of the test results.

| |image24|

The Figure gives a worked example:

| |image25|

Related calculations
''''''''''''''''''''

-  False positive rate (:math:`\alpha`) = type I error =
   :math:`1-specificity` = :math:`\frac{FP}{FP + TN}` =
   :math:`\frac{180}{180+1820}` = 9%

-  False negative rate (:math:`\beta`) = type II error =
   :math:`1−sensitivity` = :math:`\frac{FN}{TP + FN}` =
   :math:`\frac{10}{20+10}` = 33%

-  Power = sensitivity = :math:`1−\beta`

-  Likelihood ratio positive = :math:`\frac{sensitivity}{1−specificity}`
   = :math:`\frac{66.67\%}{1−91\%}` = 7.4

-  Likelihood ratio negative = :math:`\frac{1−sensitivity}{specificity}`
   = :math:`\frac{1−66.67\%}{91\%}` = 0.37

Hence with large numbers of false positives and few false negatives, a
positive FOB screen test is in itself poor at confirming cancer (PPV =
10%) and further investigations must be undertaken; it did, however,
correctly identify 66.7% of all cancers (the sensitivity). However as a
screening test, a negative result is very good at reassuring that a
patient does not have cancer (NPV = 99.5%) and at this initial screen
correctly identifies 91% of those who do not have cancer (the
specificity).

Large Sample Tests 
--------------------

Here I give an overview of the most common statistical tests for
different combinations of data. This overview is taken from .

.. [table:tests]


.. |image21| image:: ../Images/power1.png
    :scale: 50 %
.. |image22| image:: ../Images/power2.png
    :scale: 50 %
.. |image23| image:: ../Images/Sensitivity_Specificity_Diagram.png
    :scale: 50 %
.. |image24| image:: ../Images/Sensitivity_Specificity.png
    :scale: 75 %
.. |image25| image:: ../Images/Sensitivity_Specificity_Example.png
    :scale: 75 %

