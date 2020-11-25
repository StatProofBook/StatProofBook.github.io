---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-15 12:34:00

title: "Cumulative distribution function of the gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Cumulative distribution function"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Incomplete gamma function"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-10-29"
    url: "https://en.wikipedia.org/wiki/Incomplete_gamma_function#Definition"

proof_id: "P178"
shortcut: "gam-cdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a positive [random variable](/D/rvar) following a [gamma distribution](/D/gam):

$$ \label{eq:gam}
X \sim \mathrm{Gam}(a, b) \; .
$$

Then, the [cumulative distribution function](/D/cdf) of $X$ is

$$ \label{eq:gam-cdf}
F_X(x) = \frac{\gamma(a,bx)}{\Gamma(a)}
$$

where $\Gamma(x)$ is the gamma function and $\gamma(s,x)$ is the lower incomplete gamma function.


**Proof:** The [probability density function of the gamma distribution](/P/gam-pdf) is:

$$ \label{eq:gam-pdf}
f_X(x) = \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x] \; .
$$

Thus, the [cumulative distribution function](/D/cdf) is:

$$ \label{eq:gam-cdf-s1}
\begin{split}
F_X(x) &= \int_{0}^{x} \mathrm{Gam}(z; a, b) \, \mathrm{d}z \\
&= \int_{0}^{x} \frac{b^a}{\Gamma(a)} z^{a-1} \exp[-b z] \, \mathrm{d}z \\
&= \frac{b^a}{\Gamma(a)} \int_{0}^{x} z^{a-1} \exp[-b z] \, \mathrm{d}z \; .
\end{split}
$$

Substituting $t = b z$, i.e. $z = t/b$, this becomes:

$$ \label{eq:gam-cdf-s2}
\begin{split}
F_X(x) &= \frac{b^a}{\Gamma(a)} \int_{b \cdot 0}^{b x} \left(\frac{t}{b}\right)^{a-1} \exp\left[-b \left(\frac{t}{b}\right)\right] \, \mathrm{d}\left(\frac{t}{b}\right) \\
&= \frac{b^a}{\Gamma(a)} \cdot \frac{1}{b^{a-1}} \cdot \frac{1}{b} \int_{0}^{b x} t^{a-1} \exp[-t] \, \mathrm{d}t \\
&= \frac{1}{\Gamma(a)} \int_{0}^{b x} t^{a-1} \exp[-t] \, \mathrm{d}t \; .
\end{split}
$$

With the definition of the lower incomplete gamma function

$$ \label{eq:low-inc-gam-fct}
\gamma(s,x) = \int_{0}^{x} t^{s-1} \exp[-t] \, \mathrm{d}t \; ,
$$

we arrive at the final result given by equation \eqref{eq:gam-cdf}:

$$ \label{eq:gam-cdf-qed}
F_X(x) = \frac{\gamma(a,bx)}{\Gamma(a)} \; .
$$