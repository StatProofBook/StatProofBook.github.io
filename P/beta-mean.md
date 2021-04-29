---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-04-29 09:12:00

title: "Mean of the beta distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Beta distribution"
theorem: "Mean"

sources:
  - authors: "Boer Commander"
    year: 2020
    title: "Beta Distribution Mean and Variance Proof"
    in: "YouTube"
    pages: "retrieved on 2021-04-29"
    url: "https://www.youtube.com/watch?v=3OgCcnpZtZ8"

proof_id: "P228"
shortcut: "beta-mean"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [beta distribution](/D/beta):

$$ \label{eq:beta}
X \sim \mathrm{Bet}(\alpha, \beta) \; .
$$

Then, the [mean or expected value](/D/mean) of $X$ is

$$ \label{eq:beta-mean}
\mathrm{E}(X) = \frac{\alpha}{\alpha + \beta} \; .
$$


**Proof:** The [expected value](/D/mean) is the probability-weighted average over all possible values:

$$ \label{eq:mean}
\mathrm{E}(X) = \int_{\mathcal{X}} x \cdot f_X(x) \, \mathrm{d}x \; .
$$

The [probability density function of the beta distribution](/P/beta-pdf) is

$$ \label{eq:beta-pdf}
f_X(x) = \frac{1}{\mathrm{B}(\alpha, \beta)} \, x^{\alpha-1} \, (1-x)^{\beta-1}, \quad 0 \leq x \leq 1
$$

where the beta function is given by a ratio gamma functions:

$$ \label{eq:beta-fct}
\mathrm{B}(\alpha, \beta) = \frac{\Gamma(\alpha) \cdot \Gamma(\beta)}{\Gamma(\alpha+\beta)} \; .
$$

Combining \eqref{eq:mean}, \eqref{eq:beta-pdf} and \eqref{eq:beta-fct}, we have:

$$ \label{eq:beta-mean-s1}
\begin{split}
\mathrm{E}(X) &= \int_{0}^{1} x \cdot \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha) \cdot \Gamma(\beta)} \, x^{\alpha-1} \, (1-x)^{\beta-1} \, \mathrm{d}x \\
&= \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)} \cdot \frac{\Gamma(\alpha+1)}{\Gamma(\alpha+1+\beta)} \int_{0}^{1} \frac{\Gamma(\alpha+1+\beta)}{\Gamma(\alpha+1) \cdot \Gamma(\beta)} \, x^{(\alpha+1)-1} \, (1-x)^{\beta-1} \, \mathrm{d}x \; .
\end{split}
$$

Employing the relation $\Gamma(x+1) = \Gamma(x) \cdot x$, we have

$$ \label{eq:beta-mean-s2}
\begin{split}
\mathrm{E}(X) &= \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)} \cdot \frac{\alpha \cdot \Gamma(\alpha)}{(\alpha+\beta) \cdot \Gamma(\alpha+\beta)} \int_{0}^{1} \frac{\Gamma(\alpha+1+\beta)}{\Gamma(\alpha+1) \cdot \Gamma(\beta)} \, x^{(\alpha+1)-1} \, (1-x)^{\beta-1} \, \mathrm{d}x \\
&= \frac{\alpha}{\alpha+\beta} \int_{0}^{1} \frac{\Gamma(\alpha+1+\beta)}{\Gamma(\alpha+1) \cdot \Gamma(\beta)} \, x^{(\alpha+1)-1} \, (1-x)^{\beta-1} \, \mathrm{d}x
\end{split}
$$

and again using the [density of the beta distribution](/P/beta-pdf), we get

$$ \label{eq:beta-mean-s3}
\begin{split}
\mathrm{E}(X) &= \frac{\alpha}{\alpha+\beta} \int_{0}^{1} \mathrm{Bet}(x; \alpha+1, \beta) \, \mathrm{d}x \\
&= \frac{\alpha}{\alpha+\beta} \; .
\end{split}
$$