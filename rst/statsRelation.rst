.. image:: ..\Images\title_relations.png
    :height: 100 px

.. Relation Between Two Continuous Variables
.. =========================================

If we have two related variables, the *correlation* measures the
association between the two variables. In contrast, a *linear
regression* is used for the prediction of the value of one variable from
another. If we want to compare more than two groups of variables, we
have to use a technique known as *Analysis of Variance (ANOVA)*.

Correlation
-----------

Correlation Coefficient
~~~~~~~~~~~~~~~~~~~~~~~

If the two variables are normally distributed, the standard measure of
determining the *correlation coefficient*, often ascribed to *Pearson* ,
is

.. math::

   \label{eq:pearson}
     r = \frac{\sum\limits_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum\limits_{i=1}^n (X_i - \bar{X})^2} \sqrt{\sum\limits_{i=1}^n (Y_i - \bar{Y})^2}}

Pearson’s correlation coefficient, sometimes also referred to as
*population correlation coefficient*, can take any value from -1 to +1.
Examples are given in the figure below. Note that the formula
for the correlation coefficient is symmetrical between :math:`x` and
:math:`y`.

Coefficient of determination
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *coefficient of determination*  or :math:`R^2` is the square of the correlation.

The :math:`R^2` value is the proportion of variation in the dependent variable that can be explained by the variation in the independent variable. It is easier to interpret than the correlation coefficient r: Values of :math:`R^2` close to 1 are good, values close to 0 are poor.

For multiple regression, the *adjusted :math:`R^2`* value (written as :math:`\bar{R}^2`) is often used instead of :math:`R^2`:

.. math::

      \bar{R}^2 = 1 - (1 - R^2)\frac{n - 1}{n - p - 1}

where *n* is the sample size and *p* is the number of independent variables.

How large :math:`R^2` or :math:`\bar{R}^2` must be to be considered good depends on the discipline. They are usually expected to be larger in the physical sciences than it is in biology or the social sciences. In finance or marketing, it also depends on what is being modeled.

Caution: the sample correlation and :math:`R^2` are misleading if there is a nonlinear relationship between the independent and dependent variables!



| |image26|

*Several sets of (x, y) points, with the correlation coecient of x and y for each set.
Note that the correlation reects the non-linearity and direction of a linear relationship (top
row), but not the slope of that relationship (middle), nor many aspects of nonlinear relationships
(bottom). N.B.: the gure in the center has a slope of 0 but in that case the correlation
coecient is undened because the variance of Y is zero. (From: Wikipedia)*

Rank correlation 
~~~~~~~~~~~~~~~~~~

If the data distribution is not normal, a different approach is
necessary. In that case one can rank the set of subjects for each
variable and compare the orderings. There are two commonly used methods
of calculating the rank correlation.

-  *Spearman's :math:`\rho`*, which is exactly the same as the Pearson
   correlation coefficient :math:`r` calculated on the ranks of the
   observations.

-  *Kendall's :math:`\tau`*.

Regression
----------

We can use the method of *regression* when we want to predict the value
of one variable from the other.

| |image27|

*Linear regression. (From Wikipedia)*

When we search for the best-fit line to a given :math:`(x_i,y_i)`
dataset, we are looking for the parameters :math:`(k,d)` which minimize
the sum of the squared *residuals* :math:`\epsilon_i` in

.. math::

   \label{eq:simpleRegression}
     y_i = k * x_i + d + \epsilon_i

where :math:`k` is the *slope* or *inclination* of the line, and
:math:`d` the *intercept*. This is in fact just the one-dimensional
example of the more general technique, which is described in the next
section. Note that in contrast to the correlation, this relationship
between :math:`x` and :math:`y` is no more symmetrical: it is assumed
that the :math:`x-`\ values are known exactly, and that all the
variability lies in the residuals.

| |image28|

*Best-fit linear regression line (red) and residuals (black).*

Introduction
~~~~~~~~~~~~

Given a data set :math:`\{y_i,\, x_{i1}, \ldots, x_{ip}\}_{i=1}^n`
of :math:`n` statistical units, a linear regression model assumes that
the relationship between the dependent variable :math:`y_i` and the
:math:`p`-vector of regressors :math:`x_i` is linear. This relationship
is modelled through a *disturbance term* or *error variable*
:math:`\epsilon_i`, an unobserved random variable that adds noise to the
linear relationship between the dependent variable and regressors. Thus
the model takes the form

.. math::

   \label{eq:regression}
      y_i = \beta_1   x_{i1} + \cdots + \beta_p x_{ip} + \varepsilon_i
      = \mathbf{x}^{\rm T}_i\boldsymbol\beta + \varepsilon_i,
      \qquad i = 1, \ldots, n,

where :math:`^T` denotes the transpose, so that :math:`x_i^T\beta` is
the inner product between vectors :math:`x_i` :math:`\beta`.

Often these :math:`n` equations are stacked together and written in
vector form as

.. math:: \mathbf{y} = \mathbf{X}\boldsymbol\beta + \boldsymbol\varepsilon, \,

where

.. math::

   \mathbf{y} = \begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{pmatrix}, \quad
      \mathbf{X} = \begin{pmatrix} \mathbf{x}^{\rm T}_1 \\ \mathbf{x}^{\rm T}_2 \\ \vdots \\ \mathbf{x}^{\rm T}_n \end{pmatrix}
      = \begin{pmatrix} x_{11} & \cdots & x_{1p} \\
      x_{21} & \cdots & x_{2p} \\
      \vdots & \ddots & \vdots \\
      x_{n1} & \cdots & x_{np}
      \end{pmatrix}, \quad
      \boldsymbol\beta = \begin{pmatrix} \beta_1 \\ \vdots \\ \beta_p \end{pmatrix}, \quad
      \boldsymbol\varepsilon = \begin{pmatrix} \varepsilon_1 \\ \varepsilon_2 \\ \vdots \\ \varepsilon_n \end{pmatrix}.

Some remarks on terminology and general use:

-  :math:`y_i` is called the *regressand*, *endogenous variable*,
   *response variable*, *measured variable*, or *dependent variable*.
   The decision as to which variable in a data set is modeled as the
   dependent variable and which are modeled as the independent variables
   may be based on a presumption that the value of one of the variables
   is caused by, or directly influenced by the other variables.
   Alternatively, there may be an operational reason to model one of the
   variables in terms of the others, in which case there need be no
   presumption of causality.

-  :math:`\mathbf{x}_i` are called *regressors*, *exogenous variables*,
   *explanatory variables*, *covariates*, *input variables*, *predictor
   variables*, or *independent variables*, but not to be confused with
   *independent random variables*. The matrix :math:`\mathbf{X}` is
   sometimes called the *design matrix*.

   -  Usually a constant is included as one of the regressors. For
      example we can take :math:`x_{i1}=1` for :math:`i=1,...,n`. The
      corresponding element of :math:`\beta` is called the *intercept*.
      Many statistical inference procedures for linear models require an
      intercept to be present, so it is often included even if
      theoretical considerations suggest that its value should be zero.

   -  Sometimes one of the regressors can be a non-linear function of
      another regressor or of the data, as in polynomial regression and
      segmented regression. The model remains linear as long as it is
      linear in the parameter vector :math:`\beta`.

   -  The regressors :math:`x_{ij}` may be viewed either as random
      variables, which we simply observe, or they can be considered as
      predetermined fixed values which we can choose. Both
      interpretations may be appropriate in different cases, and they
      generally lead to the same estimation procedures; however
      different approaches to asymptotic analysis are used in these two
      situations.

-  :math:`\boldsymbol\beta\,` is a :math:`p`-dimensional *parameter
   vector*. Its elements are also called *effects*, or *regression
   coefficients*. Statistical estimation and inference in linear
   regression focuses on :math:`\beta`.

-  :math:`\varepsilon_i\,` is called the *error term*, *disturbance
   term*, or *noise*. This variable captures all other factors which
   influence the dependent variable :math:`y_i` other than the
   regressors :math:`x_i`. The relationship between the error term and
   the regressors, for example whether they are correlated, is a crucial
   step in formulating a linear regression model, as it will determine
   the method to use for estimation.

-  If :math:`i=1` and :math:`p=1` in Eq.[eq:regression], we have a
   *simple linear regression*, corresponding to
   Eq.[eq:simpleRegression]. If :math:`i>1` we talk about *multilinear
   regression* or *multiple linear regression* .

*Example*. Consider a situation where a small ball is being tossed up in
the air and then we measure its heights of ascent :math:`h_i` at various
moments in time :math:`t_i`. Physics tells us that, ignoring the drag,
the relationship can be modelled as :

.. math:: h_i = \beta_1 t_i + \beta_2 t_i^2 + \varepsilon_i,

where :math:`\beta_1` determines the initial velocity of the ball,
:math:`\beta_2` is proportional to the standard gravity, and
:math:`\epsilon_i` is due to measurement errors. Linear regression can
be used to estimate the values of :math:`\beta_1` and :math:`\beta_2`
from the measured data. This model is non-linear in the time variable,
but it is linear in the parameters :math:`\beta_1` and :math:`\beta_2`;
if we take regressors
:math:`\mathbf{x}_i = (x_{i1},x_{i2}) = (t_i,t_i^2)`, the model takes on
the standard form :
:math:`h_i = \mathbf{x}^{\rm T}_i\boldsymbol\beta + \varepsilon_i.`

Assumptions
~~~~~~~~~~~

To use the technique of linear regression, five assumptions should be
fulfilled:

-  The errors in the data values (i.e. the deviations from average) are
   independent from one another.

-  The model must be appropriate. (A linear regression does not properly
   describe a quadratic curve.)

-  The *independent variables* (i.e. :math:`x`) are exactly known.

-  The variance of the *dependent variable* (i.e. :math:`y`) is the same
   for all values of :math:`x`.

-  The distribution of :math:`y` is approximately normal for all values
   of :math:`x`.

(See also the ipython notebook `multivariate.ipynb <http://nbviewer.ipython.org/url/raw.github.com/thomas-haslwanter/statsintro/master/ipynb/multivariate.ipynb>`_)

.. literalinclude:: ..\Code\multivariate.py

| |image29|

*The sets in the Anscombe's quartet have the same linear regression line but are
themselves very different.*

| |image30|

*Regression, with condence intervals for the mean, as well as for the predicted data.*

Since to my knowledge there exists no program in the Python standard
library (or numpy, scipy) to calculate the confidence intervals for a
regression line, I include my corresponding program *lineFit.py*.
The output of this program is shown in the figure below.
This program also shows how Python programs intended for
distribution should be documented.

.. literalinclude:: ..\Code\fitLine.py

.. [4]
   This section has been taken from Wikipedia

.. |image24| image:: ../Images/Sensitivity_Specificity.png
    :scale: 50 %
.. |image25| image:: ../Images/Sensitivity_Specificity_Example.png
    :scale: 50 %
.. |image26| image:: ../Images/Correlation_examples2.png
    :scale: 50 %
.. |image27| image:: ../Images/Linear_regression.png
    :scale: 50 %
.. |image28| image:: ../Images/residuals_linreg.png
    :scale: 50 %
.. |image29| image:: ../Images/Anscombes_quartet.png
    :scale: 50 %
.. |image30| image:: ../Images/regression_wLegend.png
    :scale: 50 %
