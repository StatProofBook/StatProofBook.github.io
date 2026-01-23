---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-10-24 13:45:52

title: "Median of the beta distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Beta distribution"
theorem: "Median"

sources:
  - authors: "Wikipedia"
    year: 2025
    title: "Beta distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-10-24"
    url: "https://en.wikipedia.org/wiki/Beta_distribution#Median"

proof_id: "P519"
shortcut: "beta-med"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [beta distribution](/D/beta):

$$ \label{eq:beta}
X \sim \mathrm{Bet}(\alpha, \beta) \; .
$$

Then, the [median](/D/med) of $X$ is

$$ \label{eq:beta-med}
\mathrm{median}(X) = \mathrm{B}_{\alpha,\beta}^{-1}\left( \frac{\mathrm{B}(\alpha,\beta)}{2} \right) = \mathrm{I}_{1/2}^{-1}(\alpha,\beta)
$$

where $\mathrm{B}(a,b)$ is the beta function, $\mathrm{B}_{a,b}^{-1}(y)$ is the inverse function of the incomplete beta function $\mathrm{B}(x; a, b)$ and $\mathrm{I}_y^{-1}(a,b)$ is the inverse function of the regularized incomplete beta function.


**Proof:** The [median](/D/med) is the value at which the [cumulative distribution function](/D/cdf) is $1/2$:

$$ \label{eq:median}
F_X(\mathrm{median}(X)) = \frac{1}{2} \; .
$$

The [cumulative distribution function of the beta distribution](/P/beta-cdf) is

$$ \label{eq:beta-cdf}
F_X(x) = \frac{\mathrm{B}(x; \alpha, \beta)}{\mathrm{B}(\alpha, \beta)}
$$

where the incomplete beta function $\mathrm{B}(x; a, b)$ is given by

$$ \label{eq:inc-beta-fct}
\mathrm{B}(x; a, b) = \int_0^x t^{a-1} (1-t)^{b-1} \, \mathrm{d}t \; .
$$

Thus, the inverse CDF, i.e. the [quantile function](/D/qf), is

$$ \label{eq:beta-cdf-inv}
x = \mathrm{B}_{\alpha,\beta}^{-1}(p \, \mathrm{B}(\alpha,\beta))
$$

where $\mathrm{B}_{a,b}^{-1}(y)$ is the inverse function of $\mathrm{B}(x; a, b)$. Setting $p = 1/2$, we obtain:

$$ \label{eq:beta-med-qed}
\mathrm{median}(X) = \mathrm{B}_{\alpha,\beta}^{-1}\left( \frac{\mathrm{B}(\alpha,\beta)}{2} \right) \; .
$$

Alternatively, the cumulative distribution function may be written as

$$ \label{eq:beta-cdf-alt}
F_X(x) = \mathrm{I}_x(a,b)
$$

using the regularized incomplete beta function

$$ \label{eq:reg-inc-beta-fct}
\mathrm{I}_x(a,b) = \frac{\mathrm{B}(x; \alpha, \beta)}{\mathrm{B}(\alpha, \beta)}
$$

in which case the inverse CDF is

$$ \label{eq:beta-cdf-inv-alt}
x = \mathrm{I}_p^{-1}(a,b) \; ,
$$

such that the median becomes

$$ \label{eq:beta-med-qed-alt}
\mathrm{median}(X) = \mathrm{I}_{1/2}^{-1}(\alpha,\beta) \; .
$$