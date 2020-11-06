---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-06 05:30:00

title: "Probability density function of a strictly decreasing function of a continuous random variable"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Probability density function of strictly decreasing function"

sources:
  - authors: "Taboga, Marco"
    year: 2017
    title: "Functions of random variables and their distribution"
    in: "Lectures on probability and mathematical statistics"
    pages: "retrieved on 2020-11-06"
    url: "https://www.statlect.com/fundamentals-of-probability/functions-of-random-variables-and-their-distribution#hid7"

proof_id: "P188"
shortcut: "pdf-sdfct"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [continuous](/D/rvar-disc) [random variable](/D/rvar) with possible outcomes $\mathcal{X}$ and let $g(x)$ be a strictly decreasing function on the support of $X$. Then, the [probability density function](/D/pdf) of $Y = g(X)$ is given by

$$ \label{eq:pdf-sdfct}
f_Y(y) = \left\{
\begin{array}{rl}
-f_X(g^{-1}(y)) \, \frac{\mathrm{d}g^{-1}(y)}{\mathrm{d}y} \; , & \text{if} \; y \in \mathcal{Y} \\
0 \; , & \text{if} \; y \notin \mathcal{Y}
\end{array}
\right.
$$

where $g^{-1}(y)$ is the inverse function of $g(x)$ and $\mathcal{Y}$ is the set of possible outcomes of $Y$:

$$ \label{eq:Y-range}
\mathcal{Y} = \left\lbrace y = g(x): x \in \mathcal{X} \right\rbrace \; .
$$


**Proof:** The [cumulative distribution function of a strictly decreasing function](/P/cdf-sifct) is

$$ \label{eq:cdf-sdfct}
F_Y(y) = \left\{
\begin{array}{rl}
1 \; , & \text{if} \; y > \mathrm{max}(\mathcal{Y}) \\
1 - F_X(g^{-1}(y)) + \mathrm{Pr}(X = g^{-1}(y)) \; , & \text{if} \; y \in \mathcal{Y} \\
0 \; , & \text{if} \; y < \mathrm{min}(\mathcal{Y})
\end{array}
\right.
$$

Note that [for continuous random variables, the probability](/D/pdf) of point events is

$$ \label{eq:pdf-cont}
\mathrm{Pr}(X = a) = \int_a^a f_X(x) \, \mathrm{d}x = 0 \; .
$$

Because the [probability density function is the first derivative of the cumulative distribution function](/P/pdf-cdf)

$$ \label{eq:pdf-cdf}
f_X(x) = \frac{\mathrm{d}F_X(x)}{\mathrm{d}x} \; ,
$$

the [probability density function](/D/pdf) of $Y$ can be derived as follows:

1) If $y$ does not belong to the support of $Y$, $F_Y(y)$ is constant, such that

$$ \label{eq:pdf-sdfct-p1}
f_Y(y) = 0, \quad \text{if} \quad y \notin \mathcal{Y} \; .
$$

2) If $y$ belongs to the support of $Y$, then $f_Y(y)$ can be derived using the chain rule:

$$ \label{eq:pdf-sdfct-p2}
\begin{split}
f_Y(y) &\overset{\eqref{eq:pdf-cdf}}{=} \frac{\mathrm{d}}{\mathrm{d}y} F_Y(y) \\
&\overset{\eqref{eq:cdf-sdfct}}{=} \frac{\mathrm{d}}{\mathrm{d}y} \left[ 1 - F_X(g^{-1}(y)) + \mathrm{Pr}(X = g^{-1}(y)) \right] \\
&\overset{\eqref{eq:pdf-cont}}{=} \frac{\mathrm{d}}{\mathrm{d}y} \left[ 1 - F_X(g^{-1}(y)) \right] \\
&= -\frac{\mathrm{d}}{\mathrm{d}y} F_X(g^{-1}(y)) \\
&= - f_X(g^{-1}(y)) \, \frac{\mathrm{d}g^{-1}(y)}{\mathrm{d}y} \; .
\end{split}
$$

Taking together \eqref{eq:pdf-sdfct-p1} and \eqref{eq:pdf-sdfct-p2}, eventually proves \eqref{eq:pdf-sdfct}.