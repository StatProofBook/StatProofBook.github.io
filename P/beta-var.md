---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-04-29 09:31:00

title: "Variance of the beta distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Beta distribution"
theorem: "Variance"

sources:
  - authors: "Boer Commander"
    year: 2020
    title: "Beta Distribution Mean and Variance Proof"
    in: "YouTube"
    pages: "retrieved on 2021-04-29"
    url: "https://www.youtube.com/watch?v=3OgCcnpZtZ8"

proof_id: "P229"
shortcut: "beta-var"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [beta distribution](/D/beta):

$$ \label{eq:beta}
X \sim \mathrm{Bet}(\alpha, \beta) \; .
$$

Then, the [variance](/D/var) of $X$ is

$$ \label{eq:beta-var}
\mathrm{Var}(X) = \frac{\alpha \beta}{(\alpha + \beta + 1) \cdot (\alpha + \beta)^2} \; .
$$


**Proof:** The [variance](/D/var) can be expressed [in terms of expected values](/P/var-mean) as

$$ \label{eq:var-mean}
\mathrm{Var}(X) = \mathrm{E}(X^2) - \mathrm{E}(X)^2 \; .
$$

The [expected value of a beta random variable](/P/beta-mean) is

$$ \label{eq:beta-mean}
\mathrm{E}(X) = \frac{\alpha}{\alpha+\beta} \; .
$$

The [probability density function of the beta distribution](/P/beta-pdf) is

$$ \label{eq:beta-pdf}
f_X(x) = \frac{1}{\mathrm{B}(\alpha, \beta)} \, x^{\alpha-1} \, (1-x)^{\beta-1}, \quad 0 \leq x \leq 1
$$

where the beta function is given by a ratio gamma functions:

$$ \label{eq:beta-fct}
\mathrm{B}(\alpha, \beta) = \frac{\Gamma(\alpha) \cdot \Gamma(\beta)}{\Gamma(\alpha+\beta)} \; .
$$

Therefore, the expected value of a squared beta random variable becomes

$$ \label{eq:beta-sqr-mean-s1}
\begin{split}
\mathrm{E}(X^2) &= \int_{0}^{1} x^2 \cdot \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha) \cdot \Gamma(\beta)} \, x^{\alpha-1} \, (1-x)^{\beta-1} \, \mathrm{d}x \\
&= \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)} \cdot \frac{\Gamma(\alpha+2)}{\Gamma(\alpha+2+\beta)} \int_{0}^{1} \frac{\Gamma(\alpha+2+\beta)}{\Gamma(\alpha+2) \cdot \Gamma(\beta)} \, x^{(\alpha+2)-1} \, (1-x)^{\beta-1} \, \mathrm{d}x \; .
\end{split}
$$

Twice-applying the relation $\Gamma(x+1) = \Gamma(x) \cdot x$, we have

$$ \label{eq:beta-sqr-mean-s2}
\begin{split}
\mathrm{E}(X^2) &= \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)} \cdot \frac{(\alpha+1) \cdot \alpha \cdot \Gamma(\alpha)}{(\alpha+\beta+1) \cdot (\alpha+\beta) \cdot \Gamma(\alpha+\beta)} \int_{0}^{1} \frac{\Gamma(\alpha+2+\beta)}{\Gamma(\alpha+2) \cdot \Gamma(\beta)} \, x^{(\alpha+2)-1} \, (1-x)^{\beta-1} \, \mathrm{d}x \\
&= \frac{(\alpha+1) \cdot \alpha}{(\alpha+\beta+1) \cdot (\alpha+\beta)} \int_{0}^{1} \frac{\Gamma(\alpha+2+\beta)}{\Gamma(\alpha+2) \cdot \Gamma(\beta)} \, x^{(\alpha+2)-1} \, (1-x)^{\beta-1} \, \mathrm{d}x
\end{split}
$$

and again using the [density of the beta distribution](/P/beta-pdf), we get

$$ \label{eq:beta-sqr-mean-s3}
\begin{split}
\mathrm{E}(X^2) &= \frac{(\alpha+1) \cdot \alpha}{(\alpha+\beta+1) \cdot (\alpha+\beta)} \int_{0}^{1} \mathrm{Bet}(x; \alpha+2, \beta) \, \mathrm{d}x \\
&= \frac{(\alpha+1) \cdot \alpha}{(\alpha+\beta+1) \cdot (\alpha+\beta)} \; .
\end{split}
$$

Plugging \eqref{eq:beta-sqr-mean-s3} and \eqref{eq:beta-mean} into \eqref{eq:var-mean}, the variance of a beta random variable finally becomes

$$ \label{eq:beta-var-qed}
\begin{split}
\mathrm{Var}(X) &= \frac{(\alpha+1) \cdot \alpha}{(\alpha+\beta+1) \cdot (\alpha+\beta)} - \left( \frac{\alpha}{\alpha+\beta} \right)^2 \\
&= \frac{(\alpha^2+\alpha) \cdot (\alpha + \beta)}{(\alpha + \beta + 1) \cdot (\alpha + \beta)^2} - \frac{\alpha^2 \cdot (\alpha + \beta + 1)}{(\alpha + \beta + 1) \cdot (\alpha + \beta)^2} \\
&= \frac{(\alpha^3 + \alpha^2 \beta + \alpha^2 + \alpha \beta) - (\alpha^3 + \alpha^2 \beta + \alpha^2)}{(\alpha + \beta + 1) \cdot (\alpha + \beta)^2} \\
&= \frac{\alpha \beta}{(\alpha + \beta + 1) \cdot (\alpha + \beta)^2} \; .
\end{split}
$$