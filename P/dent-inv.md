---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-12-02 16:11:00

title: "Invariance of the differential entropy under addition of a constant"
chapter: "General Theorems"
section: "Information theory"
topic: "Differential entropy"
theorem: "Invariance under addition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Differential entropy"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-12"
    url: "https://en.wikipedia.org/wiki/Differential_entropy#Properties_of_differential_entropy"

proof_id: "P199"
shortcut: "dent-inv"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [continuous](/D/rvar-disc) [random variable](/D/rvar). Then, the [differential entropy](/D/dent) of $X$ remains constant under addition of a constant:

$$ \label{eq:dent-inv}
\mathrm{h}(X + c) = \mathrm{h}(X) \; .
$$


**Proof:** By definition, the [differential entropy](/D/dent) of $X$ is

$$ \label{eq:X-dent}
\mathrm{h}(X) = - \int_{\mathcal{X}} p(x) \log p(x) \, \mathrm{d}x
$$

where $p(x) = f_X(x)$ is the [probability density function](/D/pdf) of $X$.

Define the mappings between $X$ and $Y = X + c$ as

$$ \label{eq:X-Y}
Y = g(X) = X + c \quad \Leftrightarrow \quad X = g^{-1}(Y) = Y - c \; .
$$

Note that $g(X)$ is a [strictly increasing function, such that the probability density function](/P/pdf-sifct) of $Y$ is

$$ \label{eq:Y-pdf}
f_Y(y) = f_X(g^{-1}(y)) \, \frac{\mathrm{d}g^{-1}(y)}{\mathrm{d}y} \overset{\eqref{eq:X-Y}}{=} f_X(y-c) \; .
$$

Writing down the differential entropy for $Y$, we have:

$$ \label{eq:Y-dent-s1}
\begin{split}
\mathrm{h}(Y) &= - \int_{\mathcal{Y}} f_Y(y) \log f_Y(y) \, \mathrm{d}y \\
&\overset{\eqref{eq:Y-pdf}}{=} - \int_{\mathcal{Y}} f_X(y-c) \log f_X(y-c) \, \mathrm{d}y
\end{split}
$$

Substituting $x = y - c$, such that $y = x + c$, this yields:

$$ \label{eq:Y-dent-s2}
\begin{split}
\mathrm{h}(Y) &= - \int_{\left\lbrace y-c \,|\, y \in {\mathcal{Y}} \right\rbrace} f_X(x+c-c) \log f_X(x+c-c) \, \mathrm{d}(x+c) \\
&= - \int_{\mathcal{X}} f_X(x) \log f_X(x) \, \mathrm{d}x \\
&\overset{\eqref{eq:X-dent}}{=} \mathrm{h}(X) \; .
\end{split}
$$