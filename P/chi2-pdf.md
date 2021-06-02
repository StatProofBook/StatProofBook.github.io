---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-25 05:56:00

title: "Probability density function of the chi-squared distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Chi-squared distribution"
theorem: "Probability density function"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Proofs related to chi-squared distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-11-25"
    url: "https://en.wikipedia.org/wiki/Proofs_related_to_chi-squared_distribution#Derivation_of_the_pdf_for_k_degrees_of_freedom"
  - authors: "Wikipedia"
    year: 2020
    title: "n-sphere"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-11-25"
    url: "https://en.wikipedia.org/wiki/N-sphere#Volume_and_surface_area"

proof_id: "P197"
shortcut: "chi2-pdf"
username: "JoramSoch"
---


**Theorem:** Let $Y$ be a [random variable](/D/rvar) following a [chi-squared distribution](/D/chi2):

$$ \label{eq:chi2}
Y \sim \chi^{2}(k) \; .
$$

Then, the [probability density function](/D/pdf) of $Y$ is

$$ \label{eq:chi2-pdf}
f_Y(y) = \frac{1}{2^{k/2} \, \Gamma (k/2)} \, y^{k/2-1} \, e^{-y/2} \; .
$$


**Proof:** A [chi-square-distributed random variable](/D/chi2) with $k$ degrees of freedom is defined as the sum of $k$ squared [standard normal random variables](/D/snorm):

$$ \label{eq:chi2-def}
X_1, \ldots, X_k \sim \mathcal{N}(0,1) \quad \Rightarrow \quad Y = \sum_{i=1}^{k} X_i^2 \sim \chi^{2}(k) \; .
$$

Let $x_1, \ldots, x_k$ be values of $X_1, \ldots, X_k$ and consider $x = \left( x_1, \ldots, x_k \right)$ to be a point in $k$-dimensional space. Define

$$ \label{eq:y-x}
y = \sum_{i=1}^{k} x_i^2
$$

and let $f_Y(y)$ and $F_Y(y)$ be the [probability density function](/D/pdf) and [cumulative distribution function](/D/cdf) of $Y$. Because [the PDF is the first derivative of the CDF](/P/pdf-cdf), we can write:

$$ \label{eq:y-pdf-s0}
F_Y(y) = \frac{F_Y(y)}{\mathrm{d}y} \, \mathrm{d}y = f_Y(y) \, \mathrm{d}y \; .
$$

Then, the [cumulative distribution function](/D/cdf) of $Y$ can be expressed as

$$ \label{eq:y-cdf-s1}
f_Y(y) \, \mathrm{d}y = \int_{V} \prod_{i=1}^{k} \left( \mathcal{N}(x_i; 0, 1) \, \mathrm{d}x_i \right)
$$

where $\mathcal{N}(x_i; 0, 1)$ is the [probability density function](/D/pdf) of the [standard normal distribution](/D/snorm) and $V$ is the elemental shell volume at $y(x)$, which is proportional to the $(k-1)$-dimensional surface in $k$-space for which equation \eqref{eq:y-x} is fulfilled. Using the [probability density function of the normal distribution](/P/norm-pdf), equation \eqref{eq:y-cdf-s1} can be developed as follows:

$$ \label{eq:y-cdf-s2}
\begin{split}
f_Y(y) \, \mathrm{d}y &= \int_{V} \prod_{i=1}^{k} \left( \frac{1}{\sqrt{2 \pi}} \cdot \exp \left[ -\frac{1}{2} x_i^2 \right] \, \mathrm{d}x_i \right) \\
&= \int_{V} \frac{\exp \left[ -\frac{1}{2} \left( x_1^2 + \ldots + x_k^2 \right) \right]}{(2 \pi)^{k/2}} \; \mathrm{d}x_1 \, \ldots \, \mathrm{d}x_k \\
&= \frac{1}{(2 \pi)^{k/2}} \int_{V} \exp \left[ -\frac{y}{2} \right] \; \mathrm{d}x_1 \, \ldots \, \mathrm{d}x_k \; .
\end{split}
$$

Because $y$ is constant within the set $V$, it can be moved out of the integral:

$$ \label{eq:y-cdf-s3}
f_Y(y) \, \mathrm{d}y = \frac{\exp \left[ -y/2 \right]}{(2 \pi)^{k/2}} \int_{V} \; \mathrm{d}x_1 \, \ldots \, \mathrm{d}x_k \; .
$$

Now, the integral is simply the surface area of the $(k-1)$-dimensional sphere with radius $r = \sqrt{y}$, which is

$$ \label{eq:A}
A = 2 r^{k-1} \, \frac{\pi^{k/2}}{\Gamma(k/2)} \; ,
$$

times the infinitesimal thickness of the sphere, which is

$$ \label{eq:dR}
\frac{\mathrm{d}r}{\mathrm{d}y} = \frac{1}{2} y^{-1/2} \quad \Leftrightarrow \quad \mathrm{d}r = \frac{\mathrm{d}y}{2 y^{1/2}} \; .
$$

Substituting \eqref{eq:A} and \eqref{eq:dR} into \eqref{eq:y-cdf-s3}, we have:

$$ \label{eq:y-cdf-s4}
\begin{split}
f_Y(y) \, \mathrm{d}y &= \frac{\exp \left[ -y/2 \right]}{(2 \pi)^{k/2}} \cdot A \, \mathrm{d}r \\
&= \frac{\exp \left[ -y/2 \right]}{(2 \pi)^{k/2}} \cdot 2 r^{k-1} \, \frac{\pi^{k/2}}{\Gamma(k/2)} \cdot \frac{\mathrm{d}y}{2 y^{1/2}} \\
&= \frac{1}{2^{k/2} \, \Gamma(k/2)} \cdot \frac{2 \sqrt{y}^{k-1}}{2 \sqrt{y}} \cdot \exp \left[ -y/2 \right] \, \mathrm{d}y \\
&= \frac{1}{2^{k/2} \, \Gamma(k/2)} \cdot y^{\frac{k}{2}-1} \cdot \exp \left[ -\frac{y}{2} \right] \, \mathrm{d}y \; .
\end{split}
$$

From this, we get the final result in \eqref{eq:chi2-pdf}:

$$ \label{eq:y-cdf-s5}
f_Y(y) = \frac{1}{2^{k/2} \, \Gamma (k/2)} \, y^{k/2-1} \, e^{-y/2} \; .
$$
