---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-15 13:02:00

title: "Expected value of x times ln(x) for a gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Expectation of x ln x"

sources:
  - authors: "gunes"
    year: 2020
    title: "What is the expected value of x log(x) of the gamma distribution?"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2020-10-15"
    url: "https://stats.stackexchange.com/questions/457357/what-is-the-expected-value-of-x-logx-of-the-gamma-distribution"

proof_id: "P179"
shortcut: "gam-xlogx"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [gamma distribution](/D/gam):

$$ \label{eq:gam}
X \sim \mathrm{Gam}(a, b) \; .
$$

Then, the [mean or expected value](/D/mean) of $(X \cdot \ln X)$ is

$$ \label{eq:gam-xlogx}
\mathrm{E}(X \ln X) = \frac{a}{b} \left[ \psi(a) - \ln(b) \right] \; .
$$


**Proof:** With the [definition of the expected value](/D/mean), the [law of the unconscious statistician](/P/mean-lotus) and the [probability density function of the gamma distribution](/P/gam-pdf), we have:

$$ \label{eq:gam-xlogx-s1}
\begin{split}
\mathrm{E}(X \ln X) &= \int_{0}^{\infty} x \ln x \cdot \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x] \, \mathrm{d}x \\
&= \frac{1}{\Gamma(a)} \int_{0}^{\infty} \ln x \cdot \frac{b^{a+1}}{b} x^{a} \exp[-b x] \, \mathrm{d}x \\
&= \frac{\Gamma(a+1)}{\Gamma(a) \, b} \int_{0}^{\infty} \ln x \cdot \frac{b^{a+1}}{\Gamma(a+1)} x^{(a+1)-1} \exp[-b x] \, \mathrm{d}x \\
\end{split}
$$

The integral now corresponds to the [logarithmic expectation of a gamma distribution](/P/gam-logmean) with shape $a+1$ and rate $b$

$$ \label{eq:logmean-a+1}
\mathrm{E}(\ln Y) \quad \text{where} \quad Y \sim \mathrm{Gam}(a+1,b)
$$

which [is given by](/P/gam-logmean)

$$ \label{eq:gam-logmean}
\mathrm{E}(\ln Y) = \psi(a+1) - \ln(b)
$$

where $\psi(x)$ is the digamma function. Additionally employing the relation

$$ \label{eq:gam-fct}
\Gamma(x+1) = \Gamma(x) \cdot x \quad \Leftrightarrow \quad \frac{\Gamma(x+1)}{\Gamma(x)} = x \; ,
$$

the expression in equation \eqref{eq:gam-xlogx-s1} develops into:

$$ \label{eq:gam-xlogx-qed}
\mathrm{E}(X \ln X) = \frac{a}{b} \left[ \psi(a) - \ln(b) \right] \; .
$$