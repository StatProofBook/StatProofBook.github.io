---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-12-02 16:39:00

title: "Addition of the differential entropy upon multiplication with a constant"
chapter: "General Theorems"
section: "Information theory"
topic: "Differential entropy"
theorem: "Addition upon multiplication"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Differential entropy"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-12"
    url: "https://en.wikipedia.org/wiki/Differential_entropy#Properties_of_differential_entropy"

proof_id: "P200"
shortcut: "dent-add"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [continuous](/D/rvar-disc) [random variable](/D/rvar). Then, the [differential entropy](/D/dent) of $X$ increases additively upon multiplication with a constant:

$$ \label{eq:dent-add}
\mathrm{h}(aX) = \mathrm{h}(X) + \log |a| \; .
$$


**Proof:** By definition, the [differential entropy](/D/dent) of $X$ is

$$ \label{eq:X-dent}
\mathrm{h}(X) = - \int_{\mathcal{X}} p(x) \log p(x) \, \mathrm{d}x
$$

where $p(x) = f_X(x)$ is the [probability density function](/D/pdf) of $X$.

Define the mappings between $X$ and $Y = aX$ as

$$ \label{eq:X-Y}
Y = g(X) = aX \quad \Leftrightarrow \quad X = g^{-1}(Y) = \frac{Y}{a} \; .
$$

If $a > 0$, then $g(X)$ is a [strictly increasing function, such that the probability density function](/P/pdf-sifct) of $Y$ is

$$ \label{eq:Y-pdf-c1}
f_Y(y) = f_X(g^{-1}(y)) \, \frac{\mathrm{d}g^{-1}(y)}{\mathrm{d}y} \overset{\eqref{eq:X-Y}}{=} \frac{1}{a} \, f_X\left(\frac{y}{a}\right) \; ;
$$

if $a < 0$, then $g(X)$ is a [strictly decreasing function, such that the probability density function](/P/pdf-sdfct) of $Y$ is

$$ \label{eq:Y-pdf-c2}
f_Y(y) = - f_X(g^{-1}(y)) \, \frac{\mathrm{d}g^{-1}(y)}{\mathrm{d}y} \overset{\eqref{eq:X-Y}}{=} -\frac{1}{a} \, f_X\left(\frac{y}{a}\right) \; ;
$$

thus, we can write

$$ \label{eq:Y-pdf}
f_Y(y) = \frac{1}{|a|} \, f_X\left(\frac{y}{a}\right) \; .
$$

Writing down the differential entropy for $Y$, we have:

$$ \label{eq:Y-dent-s1}
\begin{split}
\mathrm{h}(Y) &= - \int_{\mathcal{Y}} f_Y(y) \log f_Y(y) \, \mathrm{d}y \\
&\overset{\eqref{eq:Y-pdf}}{=} - \int_{\mathcal{Y}} \frac{1}{|a|} \, f_X\left(\frac{y}{a}\right) \log \left[ \frac{1}{|a|} \, f_X\left(\frac{y}{a}\right) \right] \, \mathrm{d}y
\end{split}
$$

Substituting $x = y/a$, such that $y = ax$, this yields:

$$ \label{eq:Y-dent-s2}
\begin{split}
\mathrm{h}(Y) &= - \int_{\left\lbrace y/a \,|\, y \in {\mathcal{Y}} \right\rbrace} \frac{1}{|a|} \, f_X\left(\frac{ax}{a}\right) \log \left[ \frac{1}{|a|} \, f_X\left(\frac{ax}{a}\right) \right] \, \mathrm{d}(ax) \\
&= - \int_{\mathcal{X}} f_X(x) \log \left[ \frac{1}{|a|} \, f_X(x) \right] \, \mathrm{d}x \\
&= - \int_{\mathcal{X}} f_X(x) \left[ \log f_X(x) - \log |a| \right] \, \mathrm{d}x \\
&= - \int_{\mathcal{X}} f_X(x) \log f_X(x) \, \mathrm{d}x + \log |a| \int_{\mathcal{X}} f_X(x) \, \mathrm{d}x \\
&\overset{\eqref{eq:X-dent}}{=} \mathrm{h}(X) + \log |a| \; .
\end{split}
$$