---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-12 07:19:00

title: "Probability density function is first derivative of cumulative distribution function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Probability density function in terms of cumulative distribution function"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Fundamental theorem of calculus"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-11-12"
    url: "https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus#Formal_statements"

proof_id: "P191"
shortcut: "pdf-cdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [continuous](/D/rvar-disc) [random variable](/D/rvar). Then, the [probability distribution function](/D/pdf) of $X$ is the first derivative of the [cumulative distribution function](/D/cdf) of $X$:

$$ \label{eq:pdf-cdf}
f_X(x) = \frac{\mathrm{d}F_X(x)}{\mathrm{d}x} \; .
$$


**Proof:** The [cumulative distribution function in terms of the probability density function of a continuous random variable](/P/cdf-pdf) is given by:

$$ \label{eq:cdf-pdf}
F_X(x) = \int_{-\infty}^{x} f_X(t) \, \mathrm{d}t, \; x \in \mathbb{R} \; .
$$

Taking the derivative with respect to $x$, we have:

$$ \label{eq:ddx-cdf}
\frac{\mathrm{d}F_X(x)}{\mathrm{d}x} = \frac{\mathrm{d}}{\mathrm{d}x} \int_{-\infty}^{x} f_X(t) \, \mathrm{d}t \; .
$$

The fundamental theorem of calculus states that, if $f(x)$ is a continuous real-valued function defined on the interval $[a,b]$, then it holds that

$$ \label{eq:FToC-1st}
F(x) = \int_{a}^{x} f(t) \, \mathrm{d}t \quad \Rightarrow \quad F'(x) = f(x) \quad \text{for all} \quad x \in (a,b) \; .
$$

Applying \eqref{eq:FToC-1st} to \eqref{eq:cdf-pdf}, it follows that

$$ \label{eq:pdf-cdf-qed}
F_X(x) = \int_{-\infty}^{x} f_X(t) \, \mathrm{d}t \quad \Rightarrow \quad \frac{\mathrm{d}F_X(x)}{\mathrm{d}x} = f_X(x) \quad \text{for all} \quad x \in \mathbb{R} \; .
$$