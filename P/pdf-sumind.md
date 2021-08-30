---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-08-30 09:31:00

title: "Probability density function of a sum of independent discrete random variables"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Probability density function of sum of independents"

sources:
  - authors: "Taboga, Marco"
    year: 2017
    title: "Sums of independent random variables"
    in: "Lectures on probability and mathematical statistics"
    pages: "retrieved on 2021-08-30"
    url: "https://www.statlect.com/fundamentals-of-probability/sums-of-independent-random-variables"

proof_id: "P258"
shortcut: "pdf-sumind"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ be two [independent](/D/ind) [continuous](/D/rvar-disc) [random variables](/D/rvar) with possible values $\mathcal{X}$ and $\mathcal{Y}$ and let $Z = X + Y$. Then, the [probability density function](/D/pdf) of $Z$ is given by

$$ \label{eq:pdf-sumind}
\begin{split}
f_Z(z) &= \int_{-\infty}^{+\infty} f_X(z-y) f_Y(y) \, \mathrm{d}y \\
\text{or} \quad f_Z(z) &= \int_{-\infty}^{+\infty} f_Y(z-x) f_X(x) \, \mathrm{d}x
\end{split}
$$

where $f_X(x)$, $f_Y(y)$ and $f_Z(z)$ are the [probability density functions](/D/pdf) of $X$, $Y$ and $Z$.


**Proof:** The [cumulative distribution function of a sum of independent random variables](/P/cdf-sumind) is

$$ \label{eq:cdf-sumind}
F_Z(z) = \mathrm{E}\left[ F_X(z-Y) \right] \; .
$$

The [probability density function is the first derivative of the cumulative distribution function](/P/pdf-cdf), such that

$$ \label{eq:pdf-sumind-qed}
\begin{split}
f_Z(z) &= \frac{\mathrm{d}}{\mathrm{d}z} F_Z(z) \\
&= \frac{\mathrm{d}}{\mathrm{d}z} \mathrm{E}\left[ F_X(z-Y) \right] \\
&= \mathrm{E}\left[ \frac{\mathrm{d}}{\mathrm{d}z} F_X(z-Y) \right] \\
&= \mathrm{E}\left[ f_X(z-Y) \right] \\
&= \int_{-\infty}^{+\infty} f_X(z-y) f_Y(y) \, \mathrm{d}y \; .
\end{split}
$$

The second equation can be derived by switching $X$ and $Y$.