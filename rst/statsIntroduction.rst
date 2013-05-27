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

-  *numpy* ... For working with vectors and arrays.

-  *scipy* ... All the essential scientific algorithms, including those
   for statistics.

-  *matplotlib* ... The de-facto standard module for plotting and
   visualization.

-  *pandas* ... Adds *DataFrames* (imagine powerful spreadsheets) to
   Python.

-  *statsmodels* ... This one is only required if you want to look more
   into statistical modeling.

Also, make sure that you have a good programming environment! Currently, my
favorite way of programming is similar to my old Matlab style: I first get
the individual steps worked out interactively in *ipython*. `ipython
<http://ipython.org/>`_ has made enormous progess over the last few years.
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

Here an example, to get you started with Python (you find a
corresponding ipython notebook under
`getting_started.ipynb <http://nbviewer.ipython.org/url/raw.github.com/thomas-haslwanter/statsintro/master/ipynb/getting_started.ipynb>`_:

Example-Session
^^^^^^^^^^^^^^^

.. literalinclude:: ..\Code\gettingStarted.py

Pandas
~~~~~~

*Pandas* is a Python module which provides suitable data structures for
statistical analysis. The following piece of code shows you how pandas
can be used for data analysis:
(See also the ipython notebook `pandas_intro.ipynb <http://nbviewer.ipython.org/url/raw.github.com/thomas-haslwanter/statsintro/master/ipynb/pynb/pandas_intro.ipynb>`_)

.. literalinclude:: ..\Code\pandas_intro.py

Here is also a good place to introduce the short function that we will
use a number of times to simplify the reading in of data:

.. literalinclude:: ..\Code\getdata.py


