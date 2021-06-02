---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-06-27 06:44:00

title: "Variance of constant is zero"
chapter: "General Theorems"
section: "Probability theory"
topic: "Variance"
theorem: "Variance of a constant"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-06-27"
    url: "https://en.wikipedia.org/wiki/Variance#Basic_properties"

proof_id: "P124"
shortcut: "var-const"
username: "JoramSoch"
---


**Theorem:** The [variance](/D/var) of a [constant](/D/const) is zero

$$ \label{eq:var-const}
a = \text{const.} \quad \Rightarrow \quad \mathrm{Var}(a) = 0
$$

and if the [variance](/D/var) of $X$ is zero, then $X$ is a [constant](/D/const)

$$ \label{eq:var-zero}
\mathrm{Var}(X) = 0 \quad \Rightarrow \quad X = \text{const.}
$$


**Proof:**

1) A [constant](/D/const) is defined as a quantity that always has the same value. Thus, if understood as a [random variable](/D/rvar), the [expected value](/D/mean) of a constant is equal to itself:

$$ \label{eq:mean-const}
\mathrm{E}(a) = a \; .
$$

Plugged into the formula of the [variance](/D/var), we have

$$ \label{eq:var-const-s1}
\begin{split}
\mathrm{Var}(a) &= \mathrm{E}\left[ (a-\mathrm{E}(a))^2 \right] \\
&= \mathrm{E}\left[ (a-a)^2 \right] \\
&= \mathrm{E}(0) \; .
\end{split}
$$

Applied to the formula of the [expected value](/D/mean), this gives

$$ \label{eq:var-const-s2}
\mathrm{E}(0) = \sum_{x=0} x \cdot f_X(x) = 0 \cdot 1 = 0 \; .
$$

Together, \eqref{eq:var-const-s1} and \eqref{eq:var-const-s2} imply \eqref{eq:var-const}.

<br>

2) The [variance](/D/var) is defined as

$$ \label{eq:var}
\mathrm{Var}(X) = \mathrm{E}\left[ (X-\mathrm{E}(X))^2 \right] \; .
$$

Because $(X-\mathrm{E}(X))^2$ is [strictly non-negative](/P/mean-nonneg), the only way for the variance to become zero is, if the squared deviation is always zero:

$$ \label{eq:sqr-dev-zero}
(X-\mathrm{E}(X))^2 = 0 \; .
$$

This, in turn, requires that $X$ is equal to its [expected value](/D/mean)

$$ \label{eq:X-eq-E-X}
X = \mathrm{E}(X)
$$

which can only be the case, if $X$ [always has the same value](/D/const):

$$ \label{eq:X-const}
X = \text{const.}
$$