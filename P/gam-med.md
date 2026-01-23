---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-10-24 13:32:53

title: "Median of the gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Median"

sources:
  - authors: "Wikipedia"
    year: 2025
    title: "Gamma distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-10-24"
    url: "https://en.wikipedia.org/wiki/Gamma_distribution#Median_approximations_and_bounds"

proof_id: "P518"
shortcut: "gam-med"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [gamma distribution](/D/gam):

$$ \label{eq:gam}
X \sim \mathrm{Gam}(a, b) \; .
$$

Then, the [median](/D/med) of $X$ is

$$ \label{eq:gam-med}
\mathrm{median}(X) = \frac{1}{b} \gamma_a^{-1}\left( \frac{\Gamma(a)}{2} \right)
$$

where $\Gamma(x)$ is the gamma function and $\gamma_s^{-1}(y)$ is the inverse function of the lower incomplete gamma function $\gamma(s,x)$ in which the first argument is $s$.


**Proof:** The [median](/D/med) is the value at which the [cumulative distribution function](/D/cdf) is $1/2$:

$$ \label{eq:median}
F_X(\mathrm{median}(X)) = \frac{1}{2} \; .
$$

The [cumulative distribution function of the gamma distribution](/P/gam-cdf) is

$$ \label{eq:gam-cdf}
F_X(x) = \frac{\gamma(a,bx)}{\Gamma(a)}
$$

where the lower incomplete gamma function $\gamma(s,x)$ is given by

$$ \label{eq:low-inc-gam-fct}
\gamma(s,x) = \int_0^x t^{s-1} \exp(-t) \, \mathrm{d}t \; .
$$

Thus, the inverse CDF, i.e. the [quantile function](/D/qf), is

$$ \label{eq:gam-cdf-inv}
x = \frac{1}{b} \gamma_a^{-1}(p \Gamma(a))
$$

where $\gamma_a^{-1}(y)$ is the inverse function of $\gamma(a,x)$. Setting $p = 1/2$, we obtain:

$$ \label{eq:gam-med-qed}
\mathrm{median}(X) = \frac{1}{b} \gamma_a^{-1}\left( \frac{\Gamma(a)}{2} \right) \; .
$$