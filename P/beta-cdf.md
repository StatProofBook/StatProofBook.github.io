---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-19 08:01:00

title: "Cumulative distribution function of the beta distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Beta distribution"
theorem: "Cumulative distribution function"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Beta distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-11-19"
    url: "https://en.wikipedia.org/wiki/Beta_distribution#Cumulative_distribution_function"
  - authors: "Wikipedia"
    year: 2020
    title: "Beta function"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-11-19"
    url: "https://en.wikipedia.org/wiki/Beta_function#Incomplete_beta_function"

proof_id: "P195"
shortcut: "beta-cdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a positive [random variable](/D/rvar) following a [beta distribution](/D/gam):

$$ \label{eq:beta}
X \sim \mathrm{Bet}(\alpha, \beta) \; .
$$

Then, the [cumulative distribution function](/D/cdf) of $X$ is

$$ \label{eq:beta-cdf}
F_X(x) = \frac{B(x; \alpha, \beta)}{B(\alpha, \beta)}
$$

where $B(a,b)$ is the beta function and $B(x;a,b)$ is the incomplete gamma function.


**Proof:** The [probability density function of the beta distribution](/P/beta-pdf) is:

$$ \label{eq:beta-pdf}
f_X(x) = \frac{1}{\mathrm{B}(\alpha, \beta)} \, x^{\alpha-1} \, (1-x)^{\beta-1} \; .
$$

Thus, the [cumulative distribution function](/D/cdf) is:

$$ \label{eq:beta-cdf-app}
\begin{split}
F_X(x) &= \int_{0}^{x} \mathrm{Bet}(z; \alpha, \beta) \, \mathrm{d}z \\
&= \int_{0}^{x} \frac{1}{\mathrm{B}(\alpha, \beta)} \, z^{\alpha-1} \, (1-z)^{\beta-1} \, \mathrm{d}z \\
&= \frac{1}{\mathrm{B}(\alpha, \beta)} \int_{0}^{x} z^{\alpha-1} \, (1-z)^{\beta-1} \, \mathrm{d}z \; .
\end{split}
$$

With the definition of the incomplete beta function

$$ \label{eq:inc-beta-fct}
B(x;a,b) = \int_{0}^{x} t^{a-1} \, (1-t)^{b-1} \, \mathrm{d}t \; ,
$$

we arrive at the final result given by equation \eqref{eq:beta-cdf}:

$$ \label{eq:beta-cdf-qed}
F_X(x) = \frac{B(x; \alpha, \beta)}{B(\alpha, \beta)} \; .
$$