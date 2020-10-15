---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-19 06:54:00

title: "Mean of the gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Mean"

sources:
  - authors: "Turlapaty, Anish"
    year: 2013
    title: "Gamma random variable: mean & variance"
    in: "YouTube"
    pages: "retrieved on 2020-05-19"
    url: "https://www.youtube.com/watch?v=Sy4wP-Y2dmA"

proof_id: "P108"
shortcut: "gam-mean"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [gamma distribution](/D/gam):

$$ \label{eq:gam}
X \sim \mathrm{Gam}(a, b) \; .
$$

Then, the [mean or expected value](/D/mean) of $X$ is

$$ \label{eq:gam-mean}
\mathrm{E}(X) = \frac{a}{b} \; .
$$


**Proof:** The [expected value](/D/mean) is the probability-weighted average over all possible values:

$$ \label{eq:mean}
\mathrm{E}(X) = \int_{\mathcal{X}} x \cdot f_X(x) \, \mathrm{d}x \; .
$$

With the [probability density function of the gamma distribution](/P/gam-pdf), this reads:

$$ \label{eq:gam-mean-s1}
\begin{split}
\mathrm{E}(X) &= \int_{0}^{\infty} x \cdot \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x] \, \mathrm{d}x \\
&= \int_{0}^{\infty} \frac{b^a}{\Gamma(a)} x^{(a+1)-1} \exp[-b x] \, \mathrm{d}x \\
&= \int_{0}^{\infty} \frac{1}{b} \cdot \frac{b^{a+1}}{\Gamma(a)} x^{(a+1)-1} \exp[-b x] \, \mathrm{d}x \; .
\end{split}
$$

Employing the relation $\Gamma(x+1) = \Gamma(x) \cdot x$, we have

$$ \label{eq:gam-mean-s2}
\mathrm{E}(X) = \int_{0}^{\infty} \frac{a}{b} \cdot \frac{b^{a+1}}{\Gamma(a+1)} x^{(a+1)-1} \exp[-b x] \, \mathrm{d}x
$$

and again using the [density of the gamma distribution](/P/gam-pdf), we get

$$ \label{eq:gam-mean-s3}
\begin{split}
\mathrm{E}(X) &= \frac{a}{b} \int_{0}^{\infty} \mathrm{Gam}(x; a+1, b) \, \mathrm{d}x \\
&= \frac{a}{b} \; .
\end{split}
$$