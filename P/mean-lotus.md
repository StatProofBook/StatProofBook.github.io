---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-22 08:30:00

title: "Law of the unconscious statistician"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "Law of the unconscious statistician"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Law of the unconscious statistician"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-07-22"
    url: "https://en.wikipedia.org/wiki/Law_of_the_unconscious_statistician#Proof"
  - authors: "Taboga, Marco"
    year: 2017
    title: "Transformation theorem"
    in: "Lectures on probability and mathematical statistics"
    pages: "retrieved on 2021-09-22"
    url: "https://www.statlect.com/glossary/transformation-theorem"

proof_id: "P138"
shortcut: "mean-lotus"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) and let $Y = g(X)$ be a function of this random variable.

1) If $X$ is a discrete random variable with possible outcomes $\mathcal{X}$ and [probability mass function](/D/pmf) $f_X(x)$, the [expected value](/D/mean) of $g(X)$ is

$$ \label{eq:mean-lotus-disc}
\mathrm{E}[g(X)] = \sum_{x \in \mathcal{X}} g(x) f_X(x) \; .
$$

2) If $X$ is a continuous random variable with possible outcomes $\mathcal{X}$ and [probability density function](/D/pdf) $f_X(x)$, the [expected value](/D/mean) of $g(X)$ is

$$ \label{eq:mean-lotus-cont}
\mathrm{E}[g(X)] = \int_{\mathcal{X}} g(x) f_X(x) \, \mathrm{d}x \; .
$$


**Proof:** Suppose that $g$ is differentiable and that its inverse $g^{-1}$ is monotonic.

1) The [expected value](/D/mean) of $Y = g(X)$ is defined as

$$ \label{eq:mean-lotus-disc-s1}
\mathrm{E}[Y] = \sum_{y \in \mathcal{Y}} y \, f_Y(y) \; .
$$

Writing the probability mass function $f_Y(y)$ in terms of $y = g(x)$, we have:

$$ \label{eq:mean-lotus-disc-s2}
\begin{split}
\mathrm{E}[g(X)] &= \sum_{y \in \mathcal{Y}} y \, \mathrm{Pr}(g(x) = y) \\
&= \sum_{y \in \mathcal{Y}} y \, \mathrm{Pr}(x = g^{-1}(y)) \\
&= \sum_{y \in \mathcal{Y}} y \sum_{x = g^{-1}(y)} f_X(x) \\
&= \sum_{y \in \mathcal{Y}} \sum_{x = g^{-1}(y)} y f_X(x) \\
&= \sum_{y \in \mathcal{Y}} \sum_{x = g^{-1}(y)} g(x) f_X(x) \; .
\end{split}
$$

Finally, noting that "for all $y$, then for all $x = g^{-1}(y)$" is equivalent to "for all $x$" if $g^{-1}$ is a monotonic function, we can conclude that

$$ \label{eq:mean-lotus-disc-s3}
\mathrm{E}[g(X)] = \sum_{x \in \mathcal{X}} g(x) f_X(x) \; .
$$

<br>
2) Let $y = g(x)$. The derivative of an inverse function is

$$ \label{eq:der-inv}
\frac{\mathrm{d}}{\mathrm{d}y} (g^{-1}(y)) = \frac{1}{g'(g^{-1}(y))}
$$

Because $x = g^{-1}(y)$, this can be rearranged into

$$ \label{eq:dx-dy}
\mathrm{d}x = \frac{1}{g'(g^{-1}(y))} \, \mathrm{d}y
$$

and subsitituing \eqref{eq:dx-dy} into \eqref{eq:mean-lotus-cont}, we get

$$ \label{eq:mean-lotus-cont-s1}
\int_{\mathcal{X}} g(x) f_X(x) \, \mathrm{d}x = \int_{\mathcal{Y}} y \, f_X(g^{-1}(y)) \, \frac{1}{g'(g^{-1}(y))} \, \mathrm{d}y \; .
$$

Considering the [cumulative distribution function](/D/cdf) of $Y$, one can deduce:

$$ \label{eq:Y-cdf}
\begin{split}
F_Y(y) &= \mathrm{Pr}(Y \leq y) \\
&= \mathrm{Pr}(g(X) \leq y) \\
&= \mathrm{Pr}(X \leq g^{-1}(y)) \\
&= F_X(g^{-1}(y)) \; .
\end{split}
$$

Differentiating to get the [probability density function](/D/pdf) of $Y$, the result is:

$$ \label{eq:Y-pdf}
\begin{split}
f_Y(y) &= \frac{\mathrm{d}}{\mathrm{d}y} F_Y(y) \\
&\overset{\eqref{eq:Y-cdf}}{=} \frac{\mathrm{d}}{\mathrm{d}y} F_X(g^{-1}(y)) \\
&= f_X(g^{-1}(y)) \, \frac{\mathrm{d}}{\mathrm{d}y} (g^{-1}(y)) \\
&\overset{\eqref{eq:der-inv}}{=} f_X(g^{-1}(y)) \, \frac{1}{g'(g^{-1}(y))} \; .
\end{split}
$$

Finally, substituing \eqref{eq:Y-pdf} into \eqref{eq:mean-lotus-cont-s1}, we have:

$$ \label{eq:mean-lotus-cont-s2}
\int_{\mathcal{X}} g(x) f_X(x) \, \mathrm{d}x = \int_{\mathcal{Y}} y \, f_Y(y) \, \mathrm{d}y = \mathrm{E}[Y] = \mathrm{E}[g(X)] \; .
$$