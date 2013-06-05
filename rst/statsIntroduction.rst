.. image:: ../Images/title_introduction.png
    :height: 100 px

*"Statistics ist the explanation of variance in the light of what
remains unexplained."*

Statistics was originally invented - as so many other things - by the
famous mathematician C.F. Gauss, who said about his own work *"Ich habe
fleissig sein müssen; wer es gleichfalls ist, wird eben so weit
kommen"*. Even if your aspirations are not that high, you can get a lot
out of statistics. In fact, if your work with real data, you probably
won’t be able to avoid it. Statistics can

-  Describe variation.

-  Make quantitative statements about populations.

-  Make predictions.

**Books:** There are a number of good books about statistics:

*Douglas G. Altman. Practical Statistics for Medical Research. Chapman & Hall/CRC, 1999* 
    This is my favorite stats book. It does not talk a lot about computers
    and modeling, but gives you a terrific introduction into the field.
    Many formulations and examples in this manuscript have been taken from
    that book.

*R.H. Riffenburgh. Statistics in Medicine. Academic Press, 3rd edition, 2012* .
    A more modern book, which is more voluminous and in my opionion a bit harder to read, is

*Daniel Kaplan. Statistical Modeling: A Fresh Approach. Macalester College, 2009*
    If you are interested in a simple introduction to modern regression modeling, check out

*Dobson AJ & Barnett AG: "An Introduction to Generalized Linear Models", 3rd ed, CRC Press(2008)*
    A very good introduction to "Generalized Linear Models". If you know
    your basic statistics, this is a good, advanced starter into statistical
    modeling.

**WWW:** On the web, you find good very extensive statistics
information in English under `http://www.statsref.com/ <http://www.statsref.com/>`_. A good German
webpage on statistics and regulatory issues is
`http://www.reiter1.com/ <http://www.reiter1.com/>`_ .

**Exercises:** Many examples are already solved in the text. For the use in
lectures (or for self-test), additional exercises are provided at the end of
most chapters. For lecturers, solutions to these exercises can be provided
on demand. Please contact me directly for that via email.

**PDF-Version:** A complete PDF-version of this introduction is available
from `here <https://github.com/thomas-haslwanter/statsintro/blob/master/Data/StatsIntro.pdf>`_

Why Statistics?
---------------

Statistics will help you to

-  Clarify the question.

-  Identify the variable and the measure of that variable that will
   answer that question.

-  Determine the required sample size.

-  Find the correct analysis for your data.

-  Make predictions based on your data.

Population and samples
----------------------

While the whole *population* of a group has certain characteristics, we
can typically never measure all of them. Instead, we have to confine
ourselves to investigate a representative *sample* of this group, and
estimate the properties of the population. Great care should be used to
make the sample representative for the population you study.

Programming Matters
-------------------

Python
~~~~~~

There are three reasons why I have decided to use Python for this
lecture.

#. It is the most elegant programming language that I know.

#. It is free.

#. It is powerful.

There is a lot of good starting material on the web (see also the links
below). If you are looking for an introductory book, check out 
*D. Harms and K. McDonald. The Quick Python Book (2nd Ed).
Manning Publications Co., 2010*

Once you start programing, the internet is the best source for
documentation and for help. Personally, most of the time I just google;
thereby I stick primarily a) to the official pages, and b) to
`http://stackoverflow.com/ <http://stackoverflow.com/>`_ . Also, I have found user groups surprisingly
active and helpful!

**Links**

* http://jrjohansson.github.com/ *Lectures on scientific computing with Python. Great ipython notebooks!*

* http://docs.python.org/2/tutorial/ *The Python tutorial. The official introduction.*

* http://scipy-lectures.github.com/ *Python Scientific Lecture Notes. Pretty comprehensive.*

* http://www.greenteapress.com/thinkpython/ *ThinkPython: A free book on Python.*

* http://www.scipy.org/NumPy_for_Matlab_Users  *Start here if you have Matlab experience.*

In general, I suggest that you start out by installing a Python
distribution which includes the most important libraries. My favorites
here are `Python(x,y) <http://code.google.com/p/pythonxy/>`_ and `WinPython <http://code.google.com/p/winpython/>`_, which are very good starting points when you are using
Windows. The former one has the advantage that most available
documentation and help files also get installed locally. Mac and Unix
users should check out the installations tips from Johansson (see above).

If you decide to install things manually, you need the following modules
in addition to the Python standard library:

-  *ipython* ... For interactive work.
  
-  *numpy* ... For working with vectors and arrays.

-  *scipy* ... All the essential scientific algorithms, including those
   for statistics.

-  *matplotlib* ... The de-facto standard module for plotting and
   visualization.

-  *pandas* ... Adds *DataFrames* (imagine powerful spreadsheets) to
   Python.

-  *statsmodels* ... This one is only required if you want to look more
   into statistical modeling.

IPython
^^^^^^^

Make sure that you have a good programming environment! Currently, my
favorite way of programming is similar to my old Matlab style: I first get
the individual steps worked out interactively in `ipython
<http://ipython.org/>`_ . Ipython has made enormous progess over the last few years.
Ipython provides interactive computing with Python, similar to the commandline in Matlab. It comes with a command history, interactive data visualization, command completion, and a lot of features that make it quick and easy to try out code.
When ipython is started in *pylab mode* (which is the typical
configuration), it automatically loads numpy and matplotlib.pyplot into the
active workspace, and provides a very convenient, Matlab-like programing
environment. A very helpful new addition is the browser-based *ipython
notebook*, with support for code, text, mathematical expressions, inline
plots and other rich media. Please check out the links to the ipython
notebooks in this statistics introduction. I believe that it will  help you
to get up to speed with python much more quickly.


To write a program, I then go to either `Spyder <http://code.google.com/p/spyderlib/>`_
(which is free) or `Wing <http://wingware.com/>`_ (which is very good, but commercial).

The flexibility of Python has the "disadvantage" that it can come in
differnt flavors or coding styles. When you know the different approaches,
they are great to use. But when you get started, it can be a bit confusing.
The following section from the Matplotlib documentation may help to clarify
these things:

Matplotlib, pylab, and pyplot: how are they related?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Matplotlib** is the whole package; *pylab* is a module in matplotlib that gets installed alongside matplotlib; and *matplotlib.pyplot* is a module in matplotlib.

**Pyplot** provides the state-machine interface to the underlying plotting library in matplotlib. This means that figures and axes are implicitly and automatically created to achieve the desired plot. For example, calling plot from pyplot will automatically create the necessary figure and axes to achieve the desired plot. Setting a title will then automatically set that title to the current axes object:

::

    import matplotlib.pyplot as plt

    plt.plot(range(10), range(10))
    plt.title("Simple Plot")
    plt.show()

**Pylab** combines the pyplot functionality (for plotting) with the numpy functionality (for mathematics and for working with arrays) in a single namespace, making that namespace (or environment) even more MATLAB-like. For example, one can call the sin and cos functions just like you could in MATLAB, as well as having all the features of pyplot.

The pyplot interface is generally preferred for non-interactive plotting (i.e., scripting). The pylab interface is convenient for interactive calculations and plotting, as it minimizes typing. Note that this is what you get if you use the ipython shell with the -pylab option, which imports everything from pylab and makes plotting fully interactive.


Coding Styles in Python
^^^^^^^^^^^^^^^^^^^^^^^
In Python you will find different coding styles and usage patterns. These styles are perfectly valid and have their pros and cons. Just about all of the examples can be converted into another style and achieve the same results. The only caveat is to avoid mixing the coding styles for your own code.

Of the different styles, there are two that are officially supported. Therefore, these are the preferred ways to use matplotlib.

For the preferred pyplot style, the imports at the top of your scripts will typically be:

::

    import matplotlib.pyplot as plt
    import numpy as np

Then one calls, for example, np.arange, np.zeros, np.pi, plt.figure, plt.plot, plt.show, etc. So, a simple example in this style would be:

::

    import matplotlib.pyplot as plt
    import numpy as np
    x = np.arange(0, 10, 0.2)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()

Note that this example used pyplot's state-machine to automatically and implicitly create a figure and an axes. For full control of your plots and more advanced usage, use the pyplot interface for creating figures, and then use the object methods for the rest:

::

    import matplotlib.pyplot as plt
    import numpy as np
    x = np.arange(0, 10, 0.2)
    y = np.sin(x)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    plt.show()

Next, the same example using a pure MATLAB-style:

::

    from pylab import *
    x = arange(0, 10, 0.2)
    y = sin(x)
    plot(x, y)
    show()

So, why all the extra typing as one moves away from the pure MATLAB-style? For very simple things like this example, the only advantage is academic: the wordier styles are more explicit, more clear as to where things come from and what is going on. For more complicated applications, this explicitness and clarity becomes increasingly valuable, and the richer and more complete object-oriented interface will likely make the program easier to write and maintain.

Here an example, to get you started with Python. For interactive work, it is
simplest to use the *pylab mode*, as shown in the example below. The corresponding ipython
notebook
`getting_started.ipynb <http://nbviewer.ipython.org/url/raw.github.com/thomas-haslwanter/statsintro/master/ipynb/getting_started.ipynb>`_:
shows how numpy and matplotlib can be addressed directly. (This is common
practice when writing functions.)

Example-Session
^^^^^^^^^^^^^^^

.. literalinclude:: ..\Code\gettingStarted_ipy.py

Pandas
~~~~~~
`pandas <http://pandas.pydata.org/>`_ is a Python module which provides suitable data structures for
statistical analysis. It significantly enhances the abilities of Python for
data input, data organization, and data manipulation. In the following, I assume
that pandas has been imported with

::
    import pandas as pd

Data Input
^^^^^^^^^^

Pandas offers tools for reading and writing data between in-memory data structures and different
formats, e.g. CSV and text files, Microsoft Excel, and SQL databases. For example, if you have data
in your clipboard, you can import them directly with

::
    data = pd.io.parsers.read_clipboard()

Or data from "Sheet1" in an Excel-file "data.xls" can be read in easily with

::
    xls = pd.io.parsers.ExcelFile('data.xls')
    data = xls.parse('Sheet1')


Data Handling and Manipulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pandas offers powerful functions to handle missing data and "nans", and other kinds of data manipulation like pivoting.

To handle labeled data, pandas introduces *DataFrame* objects. A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table. It is generally the most commonly used pandas object. For example, you can use data-frames to efficiently group objects, and do a statistical evaluation of each group:

::

    x = tile([1,2,3], 4)
    y = randn(len(x))
    df = pd.DataFrame({'treatment':x, 'result':y})
    groups = df.groupby('treatment')
    print groups.mean()

produces

::

    .            result
    treatment
    1         -0.624521
    2          0.074425
    3         -0.806102

For statistical analysis, pandas becomes really powerful if you combine it with *statsmodels* (see below).

The following piece of code shows you how pandas can be used for data analysis:

(See also the ipython notebook `pandas_intro.ipynb <http://nbviewer.ipython.org/url/raw.github.com/thomas-haslwanter/statsintro/master/ipynb/pynb/pandas_intro.ipynb>`_)

.. literalinclude:: ..\Code\pandas_intro.py


Statsmodels
~~~~~~~~~~~

`statsmodels <http://statsmodels.sourceforge.net/>`_ is a Python module that provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests, and statistical data exploration. An extensive list of result statistics are available for each estimator. In its latest release (version 0.5), statsmodels also allows the formulation of models with the popular formula language also used by $R$, the leading statistics package. For example, data on the connection between academic "success", "intelligence" and "diligence" can be described with the model *'success ~ intelligence * diligence'*, which would capture the direct effect of "intelligence" and "diligence", as well as the interaction. You find more information on that topic in the section "Statistical Models".

While for complex statistical models R still has an edge, python has a much clearer and more readable syntax, and is arguably more powerful for the data manipulation often required for statistical analysis.

General Routines
~~~~~~~~~~~~~~~~

Here is also a good place to introduce the short function that we will
use a number of times to simplify the reading in of data:

.. literalinclude:: ..\Code\getdata.py


