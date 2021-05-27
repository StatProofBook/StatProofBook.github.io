---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "KU Leuven"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2020-10-12 22:15:00

title: "Chi-squared distribution is a special case of gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Chi-squared distribution"
theorem: "Special case of gamma distribution"

sources:

proof_id: "P174"
shortcut: "chi2-gam"
username: "kjpetrykowski"
---


**Theorem:** The [chi-squared distribution](/D/chi2) with $k$ degrees of freedom is a special case of the [gamma distribution](/D/gam) with shape $\frac{k}{2}$ and rate $\frac{1}{2}$:

$$ \label{eq:chi2-gam}
X \sim \mathrm{Gam}\left( \frac{k}{2}, \frac{1}{2} \right) \Rightarrow X \sim \chi^{2}(k) \; .
$$


**Proof:** The [probability density function of the gamma distribution](/P/gam-pdf) for $x > 0$, where $\alpha$ is the shape parameter and $\beta$ is the rate paramete, is as follows:

$$ \label{eq:gam-pdf}
\mathrm{Gam}(x; \alpha, \beta) = \frac{\beta^{\alpha}}{\Gamma(\alpha)} \, x^{\alpha-1} \, e^{-\beta x}
$$

If we let $\alpha = k/2$ and $\beta = 1/2$, we obtain

$$ \label{eq:gam-pdf-chi2}
\mathrm{Gam}\left(x; \frac{k}{2}, \frac{1}{2}\right) = \frac{x^{k/2-1} \, e^{-x/2}}{\Gamma(k/2) 2^{k/2}} = \frac{1}{2^{k/2} \Gamma(k/2)} \, x^{k/2-1} \, e^{-x/2}
$$

which is equivalent to the [probability density function of the chi-squared distribution](/P/chi2-pdf).