---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-29 06:21:00

title: "Probability density function of a strictly increasing function of a continuous random variable"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Probability density function of strictly increasing function"

sources:
  - authors: "Taboga, Marco"
    year: 2017
    title: "Functions of random variables and their distribution"
    in: "Lectures on probability and mathematical statistics"
    pages: "retrieved on 2020-10-29"
    url: "https://www.statlect.com/fundamentals-of-probability/functions-of-random-variables-and-their-distribution#hid4"

proof_id: "P185"
shortcut: "pdf-sifct"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [continuous](/D/rvar-disc) [random variable](/D/rvar) with possible outcomes $\mathcal{X}$ and let $g(x)$ be a strictly increasing function on the support of $X$. Then, the [probability density function](/D/pdf) of $Y = g(X)$ is given by

$$ \label{eq:pdf-sifct}
f_Y(y) = \left\{
\begin{array}{rl}
f_X(g^{-1}(y)) \, \frac{\mathrm{d}g^{-1}(y)}{\mathrm{d}y} \; , & \text{if} \; y \in \mathcal{Y} \\
0 \; , & \text{if} \; y \notin \mathcal{Y}
\end{array}
\right.
$$

where $g^{-1}(y)$ is the inverse function of $g(x)$ and $\mathcal{Y}$ is the set of possible outcomes of $Y$:

$$ \label{eq:Y-range}
\mathcal{Y} = \left\lbrace y = g(x): x \in \mathcal{X} \right\rbrace \; .
$$


**Proof:** The [cumulative distribution function of a strictly increasing function](/P/cdf-sifct) is

$$ \label{eq:cdf-sifct}
F_Y(y) = \left\{
\begin{array}{rl}
0 \; , & \text{if} \; y < \mathrm{min}(\mathcal{Y}) \\
F_X(g^{-1}(y)) \; , & \text{if} \; y \in \mathcal{Y} \\
1 \; , & \text{if} \; y > \mathrm{max}(\mathcal{Y})
\end{array}
\right.
$$

Because the [probability density function is the first derivative of the cumulative distribution function](/P/pdf-cdf)

$$ \label{eq:pdf-cdf}
f_X(x) = \frac{\mathrm{d}F_X(x)}{\mathrm{d}x} \; ,
$$

the [probability density function](/D/pdf) of $Y$ can be derived as follows:

1) If $y$ does not belong to the support of $Y$, $F_Y(y)$ is constant, such that

$$ \label{eq:pdf-sifct-p1}
f_Y(y) = 0, \quad \text{if} \quad y \notin \mathcal{Y} \; .
$$

2) If $y$ belongs to the support of $Y$, then $f_Y(y)$ can be derived using the chain rule:

$$ \label{eq:pdf-sifct-p2}
\begin{split}
f_Y(y) &\overset{\eqref{eq:pdf-cdf}}{=} \frac{\mathrm{d}}{\mathrm{d}y} F_Y(y) \\
&\overset{\eqref{eq:cdf-sifct}}{=} \frac{\mathrm{d}}{\mathrm{d}y} F_X(g^{-1}(y)) \\
&= f_X(g^{-1}(y)) \, \frac{\mathrm{d}g^{-1}(y)}{\mathrm{d}y} \; .
\end{split}
$$

Taking together \eqref{eq:pdf-sifct-p1} and \eqref{eq:pdf-sifct-p2}, eventually proves \eqref{eq:pdf-sifct}.