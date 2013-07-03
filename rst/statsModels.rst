.. image:: ..\Images\title_models.png
    :height: 100 px

.. Statistical Models

Model language 
----------------

The mini-language commonly used now in statistics to describe formulas
was first used in the languages :math:`R` and :math:`S`, but is now also
available in Python through the module *patsy*.

For instance, if we have some variable :math:`y`, and we want to regress
it against some other variables :math:`x, a, b`, and the interaction of
a and b, then we simply write

.. math:: y \sim x + a + b + a:b

The symbols in Table are used on the right hand side to
denote different interactions.

A complete set of the description is found under

Design Matrix 
~~~~~~~~~~~~~~~

Definition
^^^^^^^^^^

In a regression model, written in matrix-vector form as

.. math:: y=X\beta+ \epsilon,

the matrix :math:`X` is the *design matrix*.

Examples
^^^^^^^^

Simple Regression
'''''''''''''''''

Example of *simple linear regression* with 7 observations. Suppose there
are 7 data points :math:`\left\{ {{y_i},{x_i}} \right\}`, where
:math:`i=1,2,…,7`. The simple linear regression model is

.. math:: y_i = \beta_0 + \beta_1 x_i +\epsilon_i, \,

where :math:`\beta_0` is the y-intercept and :math:`\beta_1` is the
slope of the regression line. This model can be represented in matrix
form as

.. math::

   \begin{bmatrix}y_1 \\ y_2 \\ y_3 \\ y_4 \\ y_5 \\ y_6 \\ y_7 \end{bmatrix}
     =
     \begin{bmatrix}1 & x_1  \\1 & x_2  \\1 & x_3  \\1 & x_4  \\1 & x_5  \\1 & x_6 \\ 1 & x_7  \end{bmatrix}
     \begin{bmatrix} \beta_0 \\ \beta_1  \end{bmatrix}
     +
     \begin{bmatrix} \epsilon_1 \\ \epsilon_2 \\ \epsilon_3 \\ \epsilon_4 \\ \epsilon_5 \\ \epsilon_6 \\ \epsilon_7 \end{bmatrix}

where the first column of ones in the design matrix represents the
y-intercept term while the second column is the x-values associated with
the y-value.

Multiple Regression
'''''''''''''''''''

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

One-way ANOVA (Cell Means Model)
''''''''''''''''''''''''''''''''

Example with a one-way analysis of variance (ANOVA) with 3 groups and 7
observations. The given data set has the first three observations
belonging to the first group, the following two observations belong to
the second group and the final two observations are from the third
group. If the model to be fit is just the mean of each group, then the
model is

.. math:: y_{ij} = \mu_i + \epsilon_{ij}

which can be written

.. math::

   \begin{bmatrix}y_1 \\ y_2 \\ y_3 \\ y_4 \\ y_5 \\ y_6 \\ y_7 \end{bmatrix} =
     \begin{bmatrix}1 & 0 & 0 \\1 &0  &0 \\ 1 & 0 & 0 \\  0 & 1 & 0 \\  0 & 1 & 0 \\  0 & 0 & 1 \\  0 & 0 & 1\end{bmatrix}
     \begin{bmatrix}\mu_1 \\ \mu_2 \\ \mu_3  \end{bmatrix}
     +
     \begin{bmatrix} \epsilon_1 \\ \epsilon_2 \\ \epsilon_3 \\ \epsilon_4 \\ \epsilon_5 \\ \epsilon_6 \\ \epsilon_7 \end{bmatrix}

It should be emphasized that in this model :math:`\mu_i` represents the
mean of the :math:`i`\ th group.

One-way ANOVA (offset from reference group)
'''''''''''''''''''''''''''''''''''''''''''

The ANOVA model could be equivalently written as each group parameter
:math:`\tau_i` being an offset from some overall reference. Typically
this reference point is taken to be one of the groups under
consideration. This makes sense in the context of comparing multiple
treatment groups to a control group and the control group is considered
the "reference". In this example, group 1 was chosen to be the reference
group. As such the model to be fit is:

.. math:: y_{ij} = \mu + \tau_i + \epsilon_{ij}

with the constraint that :math:`\tau_1` is zero.

.. math::

   \begin{bmatrix}y_1 \\ y_2 \\ y_3 \\ y_4 \\ y_5 \\ y_6 \\ y_7 \end{bmatrix} =
     \begin{bmatrix}1 &0 &0 \\1 &0  &0 \\ 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \\ 1  & 0 & 1\end{bmatrix}
     \begin{bmatrix}\mu \\  \tau_2 \\ \tau_3 \end{bmatrix}
     +
     \begin{bmatrix} \epsilon_1 \\ \epsilon_2 \\ \epsilon_3 \\ \epsilon_4 \\ \epsilon_5 \\ \epsilon_6 \\ \epsilon_7 \end{bmatrix}

In this model :math:`\mu` is the mean of the reference group and
:math:`\tau_i` is the difference from group :math:`i` to the reference
group. :math:`\tau_1` and is not included in the matrix because its
difference from the reference group (itself) is necessarily zero.

Example 1: Program Effectiveness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this rather simple example we use data from Spector and Mazzeo (1980), to estimate a linear regression model with statsmodels.

.. literalinclude:: ..\Code\regSpector.py

Example 2: Linear Models
~~~~~~~~~~~~~~~~~~~~~~~~

This second set of examples is based heavily on Jonathan Taylor's class notes that use R. The following notebook introduces the use of pandas and the formula framework in statsmodels in the context of linear modeling:

Ipython notebook `statsIntro_linearModels.ipynb <http://nbviewer.ipython.org/url/raw.github.com/thomas-haslwanter/statsintro/master/ipynb/statsIntro_linearModels.ipynb>`_


Assumptions 
-------------

Standard linear regression models with standard estimation techniques
make a number of assumptions about the predictor variables, the response
variables and their relationship. Numerous extensions have been
developed that allow each of these assumptions to be relaxed (i.e.
reduced to a weaker form), and in some cases eliminated entirely. Some
methods are general enough that they can relax multiple assumptions at
once, and in other cases this can be achieved by combining different
extensions. Generally these extensions make the estimation procedure
more complex and time-consuming, and may also require more data in order
to get an accurate model.

The following are the major assumptions made by standard linear
regression models with standard estimation techniques (e.g. ordinary
least squares):

-  **Weak exogeneity**. This essentially means that the predictor
   variables :math:`x` can be treated as fixed values, rather than
   random variables. This means, for example, that the predictor
   variables are assumed to be error-free, that is they are not
   contaminated with measurement errors. Although not realistic in many
   settings, dropping this assumption leads to significantly more
   difficult errors-in-variables models.

-  **Linearity**. This means that the mean of the response variable is a
   linear combination of the parameters (regression coefficients) and
   the predictor variables. Note that this assumption is much less
   restrictive than it may at first seem. Because the predictor
   variables are treated as fixed values (see above), linearity is
   really only a restriction on the parameters. The predictor variables
   themselves can be arbitrarily transformed, and in fact multiple
   copies of the same underlying predictor variable can be added, each
   one transformed differently. This trick is used, for example, in
   polynomial regression, which uses linear regression to fit the
   response variable as an arbitrary polynomial function (up to a given
   rank) of a predictor variable. This makes linear regression an
   extremely powerful inference method. In fact, models such as
   polynomial regression are often "too powerful", in that they tend to
   overfit the data. As a result, some kind of regularization must
   typically be used to prevent unreasonable solutions coming out of the
   estimation process. Common examples are ridge regression and lasso
   regression. Bayesian linear regression can also be used, which by its
   nature is more or less immune to the problem of overfitting. (In
   fact, ridge regression and lasso regression can both be viewed as
   special cases of Bayesian linear regression, with particular types of
   prior distributions placed on the regression coefficients.)

-  **Constant variance** (aka *homoscedasticity*). This means that
   different response variables have the same variance in their errors,
   regardless of the values of the predictor variables. In practice this
   assumption is invalid (i.e. the errors are heteroscedastic) if the
   response variables can vary over a wide scale. In order to determine
   for heterogeneous error variance, or when a pattern of residuals
   violates model assumptions of homoscedasticity (error is equally
   variable around the ’best-fitting line’ for all points of x), it is
   prudent to look for a "fanning effect" between residual error and
   predicted values. This is to say there will be a systematic change in
   the absolute or squared residuals when plotted against the predicting
   outcome. Error will not be evenly distributed across the regression
   line. Heteroscedasticity will result in the averaging over of
   distinguishable variances around the points to get a single variance
   that is inaccurately representing all the variances of the line. In
   effect, residuals appear clustered and spread apart on their
   predicted plots for larger and smaller values for points along the
   linear regression line, and the mean squared error for the model will
   be wrong. Typically, for example, a response variable whose mean is
   large will have a greater variance than one whose mean is small. For
   example, a given person whose income is predicted to be $100,000 may
   easily have an actual income of $80,000 or $120,000 (a standard
   deviation]] of around $20,000), while another person with a predicted
   income of $10,000 is unlikely to have the same $20,000 standard
   deviation, which would imply their actual income would vary anywhere
   between -$10,000 and $30,000. (In fact, as this shows, in many cases
   – often the same cases where the assumption of normally distributed
   errors fails – the variance or standard deviation should be predicted
   to be proportional to the mean, rather than constant.) Simple linear
   regression estimation methods give less precise parameter estimates
   and misleading inferential quantities such as standard errors when
   substantial heteroscedasticity is present. However, various
   estimation techniques (e.g. weighted least squares and
   heteroscedasticity-consistent standard errors) can handle
   heteroscedasticity in a quite general way. Bayesian linear regression
   techniques can also be used when the variance is assumed to be a
   function of the mean. It is also possible in some cases to fix the
   problem by applying a transformation to the response variable (e.g.
   fit the logarithm of the response variable using a linear regression
   model, which implies that the response variable has a log-normal
   distribution rather than a normal distribution).

-  **Independence of errors**. This assumes that the errors of the
   response variables are uncorrelated with each other. (Actual
   statistical independence is a stronger condition than mere lack of
   correlation and is often not needed, although it can be exploited if
   it is known to hold.) Some methods (e.g. generalized least squares)
   are capable of handling correlated errors, although they typically
   require significantly more data unless some sort of regularization is
   used to bias the model towards assuming uncorrelated errors. Bayesian
   linear regression is a general way of handling this issue.

-  **Lack of multicollinearity in the predictors**. For standard least
   squares estimation methods, the design matrix :math:`X` must have
   full column rank :math:`p`; otherwise, we have a condition known as
   multicollinearity in the predictor variables. This can be triggered
   by having two or more perfectly correlated predictor variables (e.g.
   if the same predictor variable is mistakenly given twice, either
   without transforming one of the copies or by transforming one of the
   copies linearly). It can also happen if there is too little data
   available compared to the number of parameters to be estimated (e.g.
   fewer data points than regression coefficients). In the case of
   multicollinearity, the parameter vector :math:`\beta` will be
   non-identifiable, it has no unique solution. At most we will be able
   to identify some of the parameters, i.e. narrow down its value to
   some linear subspace of :math:`R^p`. Methods for fitting linear
   models with multicollinearity have been developed. Note that the more
   computationally expensive iterated algorithms for parameter
   estimation, such as those used in generalized linear models, do not
   suffer from this problem — and in fact it’s quite normal to when
   handling categorical data\|categorically-valued predictors to
   introduce a separate indicator variable predictor for each possible
   category, which inevitably introduces multicollinearity.

Beyond these assumptions, several other statistical properties of the
data strongly influence the performance of different estimation methods:

-  The statistical relationship between the error terms and the
   regressors plays an important role in determining whether an
   estimation procedure has desirable sampling properties such as being
   unbiased and consistent.

-  The arrangement, or probability distribution of the predictor
   variables :math:`x` has a major influence on the precision of
   estimates of :math:`\beta`. Sampling and design of experiments are
   highly-developed subfields of statistics that provide guidance for
   collecting data in such a way to achieve a precise estimate of
   :math:`\beta`.

Interpretation
~~~~~~~~~~~~~~

A fitted linear regression model can be used to identify the
relationship between a single predictor variable :math:`x_j` and the
response variable :math:`y` when all the other predictor variables in
the model are “held fixed”. Specifically, the interpretation of
:math:`\beta_j` is the expected change in :math:`y` for a one-unit
change in :math:`x_j` when the other covariates are held fixed—that is,
the expected value of the partial derivative of :math:`y` with respect
to :math:`x_j`. This is sometimes called the ”unique effect” of
:math:`x_j` on ”y”. In contrast, the ”marginal effect” of :math:`x_j` on
:math:`y` can be assessed using a correlation coefficient or simple
linear regression model relating :math:`x_j` to :math:`y`; this effect
is the total derivative of :math:`y` with respect to :math:`x_j`.

Care must be taken when interpreting regression results, as some of the
regressors may not allow for marginal changes (such as dummy variables,
or the intercept term), while others cannot be held fixed (recall the
example from the introduction: it would be impossible to “hold
:math:`t_j` fixed” and at the same time change the value of
:math:`t_i^2`.

It is possible that the unique effect can be nearly zero even when the
marginal effect is large. This may imply that some other covariate
captures all the information in :math:`x_j`, so that once that variable
is in the model, there is no contribution of :math:`x_j` to the
variation in :math:`y`. Conversely, the unique effect of :math:`x_j` can
be large while its marginal effect is nearly zero. This would happen if
the other covariates explained a great deal of the variation of
:math:`y`, but they mainly explain variation in a way that is
complementary to what is captured by :math:`x_j`. In this case,
including the other variables in the model reduces the part of the
variability of :math:`y` that is unrelated to :math:`x_j`, thereby
strengthening the apparent relationship with :math:`x_j`.

The meaning of the expression “held fixed” may depend on how the values
of the predictor variables arise. If the experimenter directly sets the
values of the predictor variables according to a study design, the
comparisons of interest may literally correspond to comparisons among
units whose predictor variables have been “held fixed” by the
experimenter. Alternatively, the expression “held fixed” can refer to a
selection that takes place in the context of data analysis. In this
case, we “hold a variable fixed” by restricting our attention to the
subsets of the data that happen to have a common value for the given
predictor variable. This is the only interpretation of “held fixed” that
can be used in an observational study.

The notion of a “unique effect” is appealing when studying a complex
system where multiple interrelated components influence the response
variable. In some cases, it can literally be interpreted as the causal
effect of an intervention that is linked to the value of a predictor
variable. However, it has been argued that in many cases multiple
regression analysis fails to clarify the relationships between the
predictor variables and the response variable when the predictors are
correlated with each other and are not assigned following a study
design.
(See also the ipython notebook `modeling.ipynb <http://nbviewer.ipython.org/url/raw.github.com/thomas-haslwanter/statsintro/master/ipynb/modeling.ipynb>`_)

.. literalinclude:: ..\Code\modeling.py

Evaluation of for Linear Regression Models
------------------------------------------

One of the things that intimidated me about statistical modeling is the
deluge of expressions that appear when you run a modeling command. In the
following I will try to explain the most common parameters that you are
going to encounter when working with Linear Regression Models.

Definitions for Regression with Intercept
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:math:`n` is the number of observations, :math:`p` is the number of
regression parameters. For example, if you fit a straight line,
:math:`p=2`. In the following :math:`\hat{y}_i` will indicate the fitted
model values, and :math:`\bar{y}` will indicate the mean.

-  :math:`SSM = \sum_{i=1}^n (\hat{y}_i-\bar{y})^2` is the *Sum of
   Square for Model*, or the sum of squares for the regression.

-  :math:`SSE = \sum_{i=1}^n (y_i-\hat{y}_i)^2` is the *sum of Squares
   for Error*, or the sum of squares for the residuals.

-  :math:`SST = \sum_{i=1}^n (y_i-\bar{y})^2` is the *Sum of Squares
   Total*, and is equivalent to the sample variance multiplied by
   :math:`n-1`.

For multiple regression models, :math:`SSM + SSE = SST`

-  :math:`DFM = p - 1` is the *(Corrected) Degrees of Freedom for
   Model*. (The "-1" comes from the fact that we are only interested in
   the correlation, not in the absolute offset of the data.

-  :math:`DFE = n - p` is the *Degrees of Freedom for Error*

-  :math:`DFT = n - 1` is the *(Corrected) Degrees of Freedom Total*.
   The Horizontal line regression is the null hypothesis model.

For multiple regression models with intercept, DFM + DFE = DFT.

-  :math:`MSM = SSM / DFM` : *Mean of Squares for Model*

-  :math:`MSE = SSE / DFE` : *Mean of Squares for Error*. MSE is an
   unbiased estimate for :math:`\sigma^2` for multiple regression
   models.

-  :math:`MST = SST / DFT` : *Mean of Squares Total*, which is the
   sample variance of the y-variable.

The :math:`R^2` Value
~~~~~~~~~~~~~~~~~~~~~

The :math:`R^2` value indicates the proportion of variation in the
y-variable that is due to variation in the x-variables. For simple
linear regression, the :math:`R^2` value is the square of the sample
correlation :math:`r_{xy}`. For multiple linear regression with
intercept (which includes simple linear regression), the :math:`R^2`
value is defined as

.. math:: R^2 = \frac{SSM}{SST}

Many researchers prefer the adjusted :math:`\bar{R}^2` value (Eq
[eq:adjustedR2]), which is penalized for having a large number of
parameters in the model:

Here is the logic behind the definition of :math:`\bar{R}^2`:
:math:`R^2` is defined as :math:`R^2 = 1 - SSE/SST` or
:math:`1 - R^2 = SSE/SST`. To take into account the number of regression
parameters :math:`p`, define the adjusted R-squared value as

.. math:: 1- \bar{R}^2 = \frac{Variance for Error}{Variance Total}

where *Variance for Error* is estimated by :math:`SSE/DFE = SSE/(n-p)`, and *Variance Total* is estimated by :math:`SST/DFT = SST/(n-1)`. Thus,

.. math::

   \begin{aligned}
       1 - \bar{R}^2 &=& \frac{SSE/(n - p)}{SST/(n - 1)} \\
             	&=& \frac{SSE}{SST}\frac{n - 1}{n - p}\end{aligned}

so

.. math::

   \begin{aligned}
     \bar{R}^2 &=& 1 - \frac{SSE}{SST} \frac{n - 1}{(n - p} \\
       &=& 1 - (1 - R^2)\frac{n - 1}{n - p}\end{aligned}

The F-test
~~~~~~~~~~

If :math:`t_1, t_2, ... , t_m` are independent, :math:`N(0, \sigma^2)`
random variables, then :math:`\sum_{i=1}^m t_i^2` is a :math:`\chi^2`
(chi-squared) random variable with :math:`m` degrees of freedom.

For a multiple regression model with intercept,

.. math:: Y_j = \alpha + \beta_1 X_{1j} + ... + \beta_n X_{nj} + \epsilon_i = \alpha + \sum_{i=1}^n \beta_i X_{ij} + \epsilon_j = E(Y_j | X) + \epsilon_j

we want to test the following null hypothesis and alternative
hypothesis:

:math:`H_0`: :math:`\beta_1` = :math:`\beta_2` = , ... , =
:math:`\beta_n` = 0

:math:`H_1`: :math:`\beta_j \neq 0`, for at least one value of j

This test is known as the overall *F-test for regression*.

It can be shown that if :math:`H_0` is true and the residuals are
unbiased, homoscedastic, independent, and normal:

#. :math:`SSE / \sigma^2` has a :math:`\chi^2` distribution with DFE
   degrees of freedom.

#. :math:`SSM / \sigma^2` has a :math:`\chi^2` distribution with DFM
   degrees of freedom.

#. SSE and SSM are independent random variables.

If :math:`u` is a :math:`\chi^2` random variable with :math:`n` degrees
of freedom, :math:`v` is a :math:`\chi^2` random variable with :math:`m`
degrees of freedom, and :math:`u` and :math:`v` are independent, then if
:math:`F = \frac{u/n}{v/m}` has an F distribution with :math:`(n,m)`
degrees of freedom.

If H0 is true,

.. math:: F = \frac{(SSM/\sigma^2)/DFM}{(SSE/\sigma^2)/DFE} = \frac{SSM/DFM}{SSE/DFE} = \frac{MSM}{MSE},

has an F distribution with :math:`(DFM, DFE)` degrees of freedom, and is
independent of :math:`\sigma`.

Log-Likelihood Function
~~~~~~~~~~~~~~~~~~~~~~~

A very common approach in statistics is the idea of *Maximum Likelihood*
estimation. The basic idea is quite different from the *minimum square*
approach: there, the model is constant, and the errors of the response
are variable; in contrast, in the maximum likelihood approach, the data
response values are regarded as constant, and the likelihood of the
model is maximised.

For the Classical Linear Regression Model (with normal errors) we have

.. math:: \epsilon = y_i - \sum_{k=1}^n \beta_k x_{ik} = y_i - \mathbf{x_i^{'}} \cdot \boldsymbol\beta \; in \; N(0, \sigma^2)

so the probability density is given by

.. math:: p(\epsilon_i) =  \Phi (\frac{y_i - \mathbf{x_i^{'}} \cdot \boldsymbol\beta}{\sigma})

where :math:`\Phi(z)` is the standard normal probability distribution
function. The probability of independent samples is the product of the
individual probabilities

.. math:: \Pi_{total} = \prod_{i=1}^n p(\epsilon_i)

The *Log Likelihood function* is defined as

.. math::

   \begin{aligned}
     Log L &=& log(\Pi_{total}) \\
     &=& log\left[\prod_{i=1}^n \frac{1}{\sigma\sqrt{2 \pi}} \exp \left(\frac{(y_i - \mathbf{x_i^{'}} \cdot \boldsymbol\beta)^2}{2 \sigma^2}\right)\right] \\
     &=& \sum_{i=1}^n\left[log\left(\frac{1}{\sigma \sqrt{2 \pi}}\right)- \left(\frac{(y_i - \mathbf{x_i^{'}} \cdot \boldsymbol\beta)^2}{2 \sigma^2}\right)\right] \\
    &=& n log(\sigma) - n log \sqrt{2 \pi} - \frac{SSE}{2 \sigma^2}\end{aligned}

It can be shown that the maximum likelihood estimator of
:math:`\sigma^2` is

.. math:: E(\sigma^2) = \frac{SEE}{n}

With this, the maximised log likelihood is

.. math:: Max(Log L) = -\frac{n}{2} log \left(\frac{2 \pi}{n} \right) - \frac{n}{2} - \frac{n}{2} log(SSE)

and the maximised likelihood is

.. math:: Max(L) = \left( \frac{2 \pi}{n} \right)^{n/2} \cdot exp(- \frac{n}{2}) \cdot (SSE)^{-n/2}

Information Content of Statistical Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To judge the quality of your model, you should first visually inspect
the residuals. In addition, you can also use a number of numerical
criteria to assess the quality of a statistical model. These criteria
represent various approaches for balancing model accuracy with
parsimony.

We have already encountered the :math:`adjusted R^2` value (in the section on *Correlation*), which - in contrast to the :math:`R^2` value -
decreases if there are too many regressors in the model.

The *Akaike Information Criterion AIC*

.. math:: AIC = n * ln(SSE / n) + 2p

and the Schwartz or *Baysian Information Criterion BIC*

.. math:: BIC = n * ln(SSE/n) + p * ln(n)

are other commonly encountered criteria.

Analysis of Residuals
^^^^^^^^^^^^^^^^^^^^^

The command from provides some additional information about the
residuals of the model:

Omnibus
    In Multiple Regression the omnibus test is an ANOVA F test on all the
    coefficients, that is equivalent to the multiple correlations R Square
    F test. The omnibus F test is an overall test that examines model fit,
    thus rejecting the null hypothesis implies that the suggested linear
    model is not significally suitable to the data.

Skewness
    Sample skewness of the residuals, i.e. if they have a tail to the
    left or to the right. Equivalent to *stats.skew(model.resid, bias=True)*.

Kurtosis
    Sample kurtosis of the residuals, i.e. the pointedness of the data
    distribution. For normally distributed data approximately 3.
    (Equivalent to *stats.kurtosis(model.resid, fisher=False, bias=True)*)

Durbin-Watson
    A test statistic used to detect the presence of autocorrelation (a
    relationship between values separated from each other by a given
    time lag) in the residuals.

Jarque-Bera
    A goodness-of-fit test of whether sample data have the skewness and
    kurtosis matching a normal distribution.

Bootstrapping
-------------

Another type of modelling is *bootstrapping*/. Sometimes you have data
describing a distribution, but do not know what type of distribution it
is. So what can you do if you want to find out e.g. confidence values
for the mean?

The answer is bootstrapping. Bootstrapping is a scheme of *resampling*,
i.e. taking additional samples repeatedly from the initial sample, to
provide estimates of its variability. In a case where the distribution
of the initial sample is unknown, bootstrapping is of especial help in
that it provides information about the distribution.
(See also the ipython notebook `bootstrap.ipynb <http://nbviewer.ipython.org/url/raw.github.com/thomas-haslwanter/statsintro/master/ipynb/bootstrap.ipynb>`_)

.. literalinclude:: ..\Code\bootstrap.py

