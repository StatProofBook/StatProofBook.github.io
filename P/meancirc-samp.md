---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-04-20 16:38:24

title: "Circular sample mean"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "Circular sample mean"

sources:
  - authors: "Bishop CM"
    year: 2006
    title: "Periodic variables"
    in: "Pattern Recognition for Machine Learning"
    pages: "pp. 105-106, eq. 2.169"
    url: "http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf"

proof_id: "P533"
shortcut: "meancirc-samp"
username: "JoramSoch"
---


**Theorem:** Let $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$ be a [sample](/D/samp) from a [circular](/D/rvar-circ) [random variable](/D/rvar) $X$. Then, the [sample mean](/D/mean-samp) of $x$ is given by

$$ \label{eq:meancirc-samp}
\bar{x} = \arctan \left( \frac{\sum_{i=1}^n \sin x_i}{\sum_{i=1}^n \cos x_i} \right)
$$

where $\sin$ and $\cos$ are the sine and cosine function, respectively, and $\arctan$ is the arctangent function.


**Proof:** For observations of a [circular random variable](/D/rvar-circ) satisfying

$$ \label{eq:rvar-circ-samp-x}
0 \leq x_i < 2 \pi, \; i = 1,\ldots,n \; ,
$$

calculating the [sample mean as the arithmetic mean](/D/mean-samp) is not appropriate as this does not preserve the periodic nature of the random variable.

Instead and [in accordance with the definition of the circular expected value](/D/mean-circ), observation values are transformed to points on the unit circle ($r = 1$):

$$ \label{eq:rvar-circ-samp-y}
y_i = \left[ \begin{matrix} \cos x_i \\ \sin x_i \end{matrix} \right], \; i = 1,\ldots,n \; .
$$

Then, we calculate the [sample mean](/D/mean-samp) of transformed data points

$$ \label{eq:y-mean}
  \bar{y}
= \frac{1}{n} \sum_{i=1}^n y_i
= \left[ \begin{matrix} \frac{1}{n} \sum_{i=1}^n \cos x_i \\ \frac{1}{n} \sum_{i=1}^n \sin x_i \end{matrix} \right]
$$

and equating this sample mean with its polar-coordinate representation

$$ \label{eq:y-mean-pc}
  \left[ \begin{matrix} \frac{1}{n} \sum_{i=1}^n \cos x_i \\ \frac{1}{n} \sum_{i=1}^n \sin x_i \end{matrix} \right]
= \left[ \begin{matrix} \bar{r} \cos \bar{x} \\ \bar{r} \sin \bar{x} \end{matrix} \right] \; ,
$$

we obtain the solution for $\bar{x}$ by solving the equation system:

$$ \label{eq:x-mean}
\begin{split}
\frac{\bar{r} \sin \bar{x}}{\bar{r} \cos \bar{x}} &= \frac{\frac{1}{n} \sum_{i=1}^n \sin x_i}{\frac{1}{n} \sum_{i=1}^n \cos x_i} \\
\frac{\sin \bar{x}}{\cos \bar{x}} &= \frac{\sum_{i=1}^n \sin x_i}{\sum_{i=1}^n \cos x_i} \\
\tan \bar{x} &= \frac{\sum_{i=1}^n \sin x_i}{\sum_{i=1}^n \cos x_i} \\
\bar{x} &= \arctan \left( \frac{\sum_{i=1}^n \sin x_i}{\sum_{i=1}^n \cos x_i} \right) \; .
\end{split}
$$