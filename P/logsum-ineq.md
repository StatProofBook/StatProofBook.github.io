---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-09-09 02:46:00

title: "Log sum inequality"
chapter: "General Theorems"
section: "Information theory"
topic: "Shannon entropy"
theorem: "Log sum inequality"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Log sum inequality"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-09-09"
    url: "https://en.wikipedia.org/wiki/Log_sum_inequality#Proof"
  - authors: "Wikipedia"
    year: 2020
    title: "Jensen's inequality"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-09-09"
    url: "https://en.wikipedia.org/wiki/Jensen%27s_inequality#Statements"

proof_id: "P165"
shortcut: "logsum-ineq"
username: "JoramSoch"
---


**Theorem:** Let $a_1, \ldots, a_n$ and $b_1, \ldots, b_n$ be non-negative real numbers and define $a = \sum_{i=1}^{n} a_i$ and $b = \sum_{i=1}^{n} b_i$. Then, the log sum inequality states that

$$ \label{eq:logsum-ineq}
\sum_{i=1}^n a_i \, \log_c \frac{a_i}{b_i} \geq a \, \log_c \frac{a}{b} \; .
$$


**Proof:** Without loss of generality, we will use the natural logarithm, because a change in the base of the logarithm only implies multiplication by a constant:

$$ \label{eq:log-ln}
\log_c a = \frac{\ln a}{\ln c} \; .
$$

Let $f(x) = x \ln x$. Then, the left-hand side of \eqref{eq:logsum-ineq} can be rewritten as

$$ \label{eq:logsum-ineq-s2}
\begin{split}
\sum_{i=1}^n a_i \, \ln \frac{a_i}{b_i} &= \sum_{i=1}^n b_i \, f\left( \frac{a_i}{b_i} \right) \\
&= b \sum_{i=1}^n \frac{b_i}{b} \, f\left( \frac{a_i}{b_i} \right) \; .
\end{split}
$$

Because $f(x)$ is a convex function and

$$ \label{eq:sum-bi-b}
\begin{split}
\frac{b_i}{b} &\geq 0 \\
\sum_{i=1}^n \frac{b_i}{b} &= 1 \; ,
\end{split}
$$

applying Jensen's inequality yields

$$ \label{eq:logsum-ineq-s3}
\begin{split}
b \sum_{i=1}^n \frac{b_i}{b} \, f\left( \frac{a_i}{b_i} \right) &\geq b \, f\left( \sum_{i=1}^n \frac{b_i}{b} \frac{a_i}{b_i} \right) \\
&= b \, f\left( \frac{1}{b} \sum_{i=1}^n a_i \right) \\
&= b \, f\left( \frac{a}{b} \right) \\
&= a \, \ln \frac{a}{b} \; .
\end{split}
$$

Finally, combining \eqref{eq:logsum-ineq-s2} and \eqref{eq:logsum-ineq-s3}, this demonstrates \eqref{eq:logsum-ineq}.