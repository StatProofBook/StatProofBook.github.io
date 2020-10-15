---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-15 10:53:00

title: "Median"
chapter: "General Theorems"
section: "Probability theory"
topic: "Measures of central tendency"
definition: "Median"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Median"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-10-15"
    url: "https://en.wikipedia.org/wiki/Median"

def_id: "D101"
shortcut: "med"
username: "JoramSoch"
---


**Definition:** The median of a sample or random variable is the value separating the higher half from the lower half of its values.

<br>
1) Let $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$ be a [sample](/D/samp) from a [random variable](/D/rvar) $X$. Then, the median of $x$ is

$$ \label{eq:med-samp}
\mathrm{median}(x) = \left\{
\begin{array}{cl}
x_{(n+1)/2} \; , & \text{if} \; n \; \text{is odd} \\
\frac{1}{2}(x_{n/2} + x_{n/2+1}) \; , & \text{if} \; n \; \text{is even} \; ,
\end{array}
\right.
$$

i.e. the median is the "middle" number when all numbers are sorted from smallest to largest.

<br>
2) Let $X$ be a continuous [random variable](/D/rvar) with [cumulative distribution function](/D/cdf) $F_X(x)$. Then, the median of $X$ is

$$ \label{eq:med-rvar}
\mathrm{median}(X) = x, \quad \mathrm{s.t.} \quad F_X(x) = \frac{1}{2} \; ,
$$

i.e. the median is the value at which the CDF is $1/2$.