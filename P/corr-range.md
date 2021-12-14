---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-12-14 02:08:00

title: "Correlation always falls between -1 and +1"
chapter: "General Theorems"
section: "Probability theory"
topic: "Correlation"
theorem: "Range"

sources:
  - authors: "Dor Leventer"
    year: 2021
    title: "How can I simply prove that the pearson correlation coefficient is between -1 and 1?"
    in: "StackExchange Mathematics"
    pages: "retrieved on 2021-12-14"
    url: "https://math.stackexchange.com/a/4260655/480910"

proof_id: "P300"
shortcut: "corr-range"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ be two [random variables](/D/rvar). Then, the correlation of $X$ and $Y$ is between and including $-1$ and $+1$:

$$ \label{eq:corr-range}
-1 \leq \mathrm{Corr}(X,Y) \leq +1 \; .
$$


**Proof:** Consider the [variance](/D/var) of $X$ plus or minus $Y$, each divided by their [standard deviations](/D/std):

$$ \label{eq:var-XY}
\mathrm{Var}\left( \frac{X}{\sigma_X} \pm \frac{Y}{\sigma_Y} \right) \; .
$$

Because the [variance is non-negative](/P/var-nonneg), this term is larger than or equal to zero:

$$ \label{eq:var-XY-0}
0 \leq \mathrm{Var}\left( \frac{X}{\sigma_X} \pm \frac{Y}{\sigma_Y} \right) \; .
$$

Using the [variance of a linear combination](/P/var-lincomb), it can also be written as:

$$ \label{eq:var-XY-s1}
\begin{split}
\mathrm{Var}\left( \frac{X}{\sigma_X} \pm \frac{Y}{\sigma_Y} \right) &= \mathrm{Var}\left( \frac{X}{\sigma_X} \right) + \mathrm{Var}\left( \frac{Y}{\sigma_Y} \right) \pm 2 \, \mathrm{Cov}\left( \frac{X}{\sigma_X}, \frac{Y}{\sigma_Y} \right) \\
&= \frac{1}{\sigma_X^2} \mathrm{Var}(X) + \frac{1}{\sigma_Y^2} \mathrm{Var}(Y) \pm 2 \, \frac{1}{\sigma_X \sigma_Y} \, \mathrm{Cov}(X,Y) \\
&= \frac{1}{\sigma_X^2} \sigma_X^2 + \frac{1}{\sigma_Y^2} \sigma_Y^2 \pm 2 \, \frac{1}{\sigma_X \sigma_Y} \, \sigma_{XY} \; .
\end{split}
$$

Using the [relationship between covariance and correlation](/P/cov-corr), we have:

$$ \label{eq:var-XY-s2}
\mathrm{Var}\left( \frac{X}{\sigma_X} \pm \frac{Y}{\sigma_Y} \right) = 1 + 1 + \pm 2 \, \mathrm{Corr}(X,Y) \; .
$$

Thus, the combination of \eqref{eq:var-XY-0} with \eqref{eq:var-XY-s2} yields

$$ \label{eq:var-XY-ineq}
0 \leq 2 \pm 2 \, \mathrm{Corr}(X,Y)
$$

which is equivalent to

$$ \label{eq:corr-range-qed}
-1 \leq \mathrm{Corr}(X,Y) \leq +1 \; .
$$