.. image:: ../Images/title_ANOVA.png
    :height: 100 px

.. Relation Between Several Variables
.. ==================================

When we have two groups, we can ask the question: "Are they different?"
The answer is provided by hypothesis tests: by a *t-test* if the data
are normally distributed, or by a *Mann-Whitney test* otherwise. If we
want to go one step further and predict the value of one variable from
another, we have to use the technique of *linear regression*.

So what happens when we have more than two groups?

To answer the question "Are they different?" for more than two groups, we have to use the \emph{Analysis of Variance (ANOVA)-test} for data where the residuals are normally distributed. If this condition is not fulfilled, the \emph{Kruskal-Wallis Test} has to be used.

What should we do if we have paired data?

If we have matched pairs for two groups, and the differences are not
normally distributed, we can use the *Wilcoxon signed rank sum test*.
The rank test for more than two groups of matched data is the *Friedman
test*.

It may be worth mentioning that Thom Baguley suggested the following: Where
one-way repeated measures ANOVA is not appropriate, rank transformation
followed by ANOVA will provide a more robust test with greater statistical
power than the Friedman test.

An example for the application of the Friedman test: Ten professional piano
players are blindfolded, and are asked to judge the quality of three
different pianos. Each player rates each piano on a scale of 1 to 10 (1
being the lowest possible grade, and 10 the highest possible grade). The
null hypothesis is that all three pianos rate equally. To test the null
hypothesis, the Friedman test is used on the ratings of the ten piano
players.

And if we want to and predict the value of one variable *many* other
variables, linear regression has to be replaced by of *multilinear
regression* , sometimes also referred
to as *multiple linear regression*.


Two-way ANOVA
-----------------

.. index:: ANOVA-two-way

Compared to one-way ANOVAs (see :ref:`one-way ANOVAs`), the analysis with
two-way ANOVAs has a new element. We can look not only if each of the factors is
significant; we can also check if the *interaction* of the factors has a
significant influence on the distribution of the data. For sticking to the
example above, if only women with treatment B get healthy, we have a significant
interaction effect between "gender" and "treatment".

Example: two-way ANOVA 
~~~~~~~~~~~~~~~~~~~~~~~~

|ipynb| `90_anovaTwoway.ipynb <http://nbviewer.ipython.org/url/raw.github.com/thomas-haslwanter/statsintro/master/ipynb/90_anovaTwoway.ipynb>`_

|python| `anovaTwoway.py <https://github.com/thomas-haslwanter/statsintro/blob/master/Code3/anovaTwoway.py>`_

::

                        df  sum_sq mean_sq        F    PR(>F)
  C(fetus)               2  324.00  162.00  2113.10  1.05e-27
  C(observer)            3    1.19    0.39     5.21  6.497-03
  C(fetus):C(observer)   6    0.56    0.09     1.22  3.29e-01
  Residual              24    1.84    0.07      NaN       NaN
    

Multilinear Regression 
------------------------

.. index:: regression-multilinear

If you have truly independent variables, *multilinear regression* is a
straightforward extension of the simple linear regression.


Multiple Regression
~~~~~~~~~~~~~~~~~~~

Example of *multiple regression* with covariates (i.e. independent
variables) :math:`w_i` and :math:`x_i`. Again suppose that the data are
7 observations, and for each observed value to be predicted
(:math:`y_i`), there are two covariates that were also observed
:math:`w_i` and :math:`x_i`. The model to be considered is

.. math:: y_i = \beta_0 + \beta_1 w_i + \beta_2 x_i + \epsilon_i

This model can be written in matrix terms as

.. math::

   \begin{bmatrix}y_1 \\ y_2 \\ y_3 \\ y_4 \\ y_5 \\ y_6 \\ y_7 \end{bmatrix} =
       \begin{bmatrix} 1 & w_1 & x_1  \\1 & w_2 & x_2  \\1 & w_3 & x_3  \\1 & w_4 & x_4  \\1 & w_5 & x_5  \\1 & w_6 & x_6 \\ 1& w_7  & x_7  \end{bmatrix}
       \begin{bmatrix} \beta_0 \\ \beta_1 \\ \beta_2  \end{bmatrix}
       +
       \begin{bmatrix} \epsilon_1 \\ \epsilon_2 \\ \epsilon_3 \\ \epsilon_4 \\ \epsilon_5 \\ \epsilon_6 \\ \epsilon_7 \end{bmatrix}

However,  you have to watch out: if your variables may be related to each other, you have to proceed much more
carefully. For example, you may want to investigate how the prevalence of some disease correlates with age and
with income: if you do so, you have to keep in mind that age and income are most likely correlated! For
details, Kaplan(2009) gives a good introduction to that topic. Also, check out the chapter on Modeling.

|ipynb| `91_mult_regress.ipynb <http://nbviewer.ipython.org/url/raw.github.com/thomas-haslwanter/statsintro/master/ipynb/91_mult_regress.ipynb>`_

|python| `mult_regress.py <https://github.com/thomas-haslwanter/statsintro/blob/master/Code3/mult_regress.py>`_

.. |ipynb| image:: ../Images/IPython.jpg
    :scale: 50 % 
.. |python| image:: ../Images/python.jpg
    :scale: 50 % 
