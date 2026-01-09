---
layout: proof
mathjax: true

author: "Leo Hope-Kaufman"
affiliation: "Harvard University Extension School"
e_mail: "leohopekaufman@gmail.com"
date: 2026-01-02 16:47:00

title: "Chi-squared distribution is a special case of gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Chi-squared distribution"
theorem: "Special case of gamma distribution"

sources:
  - authors: "John Rice"
    year: 2007
    title: "The Moment-Generating Function"
    in: "Mathematical Statistics, Third Edition"
    pages: "p. 155 and p. A2"
    url: "https://korivernon.com/documents/MathematicalStatisticsandDataAnalysis3ed.pdf"
  - authors: "Irene Vrbik"
    year: 2025
    title: "MGF of a Gamma and Chi square"
    in: "Stat 205"
    url: "https://irene.vrbik.ok.ubc.ca/quarto/stat205/lectures/proofs/mgf-gamma.html"
  - authors: "Wikipedia"
    year: 2025
    title: "Chi-squared distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-12-26"
    url: "https://en.wikipedia.org/wiki/Chi-squared_distribution"
  - authors: "Wikipedia"
    year: 2025
    title: "Gamma distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-12-26"
    url: "https://en.wikipedia.org/wiki/Gamma_distribution"

proof_id: "P521"
shortcut: "chi2-gam2"
username: "natrium-256"
---


**Theorem:** The [chi-squared distribution](/D/chi2) with $n \in \mathbb{Z}^*$ [degrees of freedom](/D/dof) is a special case of the [gamma distribution](/D/gam) with [parameters](/D/para) $\alpha = \frac{n}{2}$, $\beta = \frac{1}{2}$ and support $t < \frac{1}{2}$. 


**Proof:** The [moment-generating function](/D/mgf) of a [gamma random variable](/D/gam) $X \sim \mathrm{Gam}(\alpha, \beta)$ is

$$ \label{eq:gam-mgf}
M_X(t) = (1-\frac{t}{\beta})^{-\alpha}, \; t < \beta, \; \beta > 0 \; .
$$

The [moment-generating function](/D/mgf) of the a [chi-squared random variable](/D/chi2) $Y \sim \chi^2_{n}$ with $n$ degrees of freedom is

$$ \label{eq:chi2-mgf}
M_Y(t) = (1-2t)^{-n/2}, \; t < \frac{1}{2} \; .
$$

If there is a [random variable](/D/rvar) $X \sim \mathrm{Gam}(n/2, 1/2)$, then

$$ \label{eq:gam-chi2-mgf}
M_X(t) = (1-\frac{t}{\frac{1}{2}})^{-(n/2)} = (1-2t)^{-n/2} = M_Y(t)
\quad \text{for} \quad
t < \frac{1}{2}
$$

"If the moment-generating function exists for $t$ in an open interval containing zero, it uniquely determines the probability distribution." (Rice, 2007, p. 155) Both moment-generating functions \eqref{eq:gam-mgf} and \eqref{eq:chi2-mgf} satisfy this condition. Specifically, $M_X(t)$ is defined for $t < \frac{1}{2}$, and for $M_Y(t)$, we have $t < \beta$ with $\beta > 0$; both of these intervals contain 0.

By the [uniqueness of the moment-generating function](/P/mgf-uniq), the chi-squared distribution with $n$ degrees of freedom is a special case of the gamma distribution with parameters $\alpha = \frac{n}{2}$ and $\beta = \frac{1}{2}$ and support $t < \frac{1}{2}$. This completes the proof.