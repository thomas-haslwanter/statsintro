.. image:: ../Images/title_preface.png
    :height: 100 px

In doing the data analysis in my own research work, I was often slowed
down by two things: 1) I did not know enough statistics, and 2) the
books available would provide a theoretical background, but no real
practical help. The book you are holding in your hands (or on your
tablet or laptop) is intended to be the book that would have solved just
this problem. It should provide enough basic understanding so you know
what you are doing; and it should provide you with the tools to do so.
In providing statistical solutions for the most basic statistical
problem, I believe that I cover at least 90% of the problems that most
physicists, biologists, and medical doctors encounter in their work. So
if you are the typical graduate student working on your degree, chances
are that you will find the solution - explanation and source-code -
here. For serious statical work, you will need to dig into the serious
statistics books and literature, which goes beyond the scope of this
book, and - to be frank - beyond my statistical knowledge.

My motivation to provide the solutions in Python are based on two
considerations. One is that I would like them to be available to
everyone. While commercial solutions like Matlab, SPSS, Minitab etc. are
available, most of us can only use them legally as long as they are in
academia. In contrast, Python is completely free, as in "free beer" The
second reason is that Python is the most beautiful coding language that
I have yet encountered; and around 2010 Python and its documentation had
matured to the point where you could use it without being a hacker. All
together, you get a free, beautiful package that allows you to do all
the statistics that at least 95% of all researchers need to do in their
lifetime. OK, for really serious statistical modeling :math:\`R\` still
sets the standard. But most of us will be more than happy with the tools
that the Python ecosystem offers today.

For whom this book is
---------------------

This book assumes that

-  you have some basic programming experience (If you have zero prior
   programming experience, you may want to start out with getting going
   with Python, using some of the great links given in the text.
   Starting programming *and* starting statistics may be a bit much at a
   time.)

-  you have some data that you want to analyze (For almost all cases, a
   working Python program is provided. All you have to do is select the
   right program, adjust it so that it reads in your data, and interpret
   the results.)

-  that you are not a statistics expert (If you are already a statistics
   expert, the online help in Python will be sufficient to allow you to
   do most of your data anlysis right away.)

The idea of this book is to give you all (or at least most of) the tools
that you will need for your statistical data analysis. Thereby I try to
provide all the background required to understand what you are doing. I
will not proof any theorems, and won't indulge in mathematics where it
is unnecessary. This approach explains why so much code is included: in
principle, you have to define our problem, select the corresponding
program, and adapt it to your needs. This should allow you to get going
quickly, even if you have little Python experience. This is also the
reason why I have not provided the software as a Python module, since I
expect that you have to tailor each program to your specific setup (data
format, etc).

How to use this book
--------------------

-  If you just want to look something up, simply go to the `HTML-version
   of the book <http://work.thaslwanter.at/Stats/html>`__.

   In the online version, code samples are marked as follows

   |ipynb| ... refers to *IPython notebooks*

   |python| ... refers to plain Python code 

-  If you want to go through it systematically, or if you prefer to read
   printed material, you may want to download the `PDF-version of the
   book <http://work.thaslwanter.at/Stats/StatsIntro.pdf>`__.

-  If you want to get the whole package, and/or if you want to
   contribute to the book, clone the `github repository of the
   book <https://github.com/thomas-haslwanter/statsintro>`__, which
   includes all the Python programs, the sample data used in the book,
   the TEX-files, RST-files, and all the images.

   If you have never used github, you might want to check out `this
   introduction to
   github <https://help.github.com/articles/set-up-git>`__. But don't be
   scared off, you can download individual files easily from your
   web-browser.

Chapter 1
    gives an introduction to the book, especially to the Python
    programming environment that we are going to use.

Chapter 2
    proceeds with an introduction to statistical analysis.

Chapter 3
    provides the basis on which statistic rests: continuous and discrete
    distribution functions.

Chapters 4-11
    form the heart of the introduction: they introduce the different
    statistical tests, and give examples (including the Python code) on
    how to use them.

Chapters 12-14
    provide an outlook to advanced statistical analysis procedures, with
    an introduction to statistical modeling in Chapter 13, and a
    presentation of the basic ideas of Bayesian Statistics in Chapter
    14.

Code samples are marked as follows

Python code samples, listed in the Appendix.

Contributor List
----------------

If you have a suggestion or correction, please send email to
thomas.haslwanter@fh-linz.at. If I make a change based on your feedback,
I will add you to the contributor list (unless you ask to be omitted).

If you include at least part of the sentence the error appears in, that
makes it easy for me to search. Page and section numbers are fine, too,
but not as easy to work with. Thanks!

-  Connor Johnson wrote a very nice blog explaining the results of
   statsmodels OLS command, which formed the basis of a large part of
   the section on *Statistical Models*.

-  To demonstrate Bayesian statistics and MCMC-models, I took the
   example of the Challenger disaster from the excellent open source
   e-book Probabilistic-Programming-and-Bayesian-Methods-for-Hackers by
   Cam Davidson Pilon.

.. |ipynb| image:: ../Images/IPython.jpg
    :scale: 50 % 
.. |python| image:: ../Images/python.jpg
    :scale: 50 % 
