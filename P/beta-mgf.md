---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-25 06:55:00

title: "Moment-generating function of the beta distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Beta distribution"
theorem: "Moment-generating function"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Beta distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-11-25"
    url: "https://en.wikipedia.org/wiki/Beta_distribution#Moment_generating_function"
  - authors: "Wikipedia"
    year: 2020
    title: "Confluent hypergeometric function"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-11-25"
    url: "https://en.wikipedia.org/wiki/Confluent_hypergeometric_function#Kummer's_equation"

proof_id: "P198"
shortcut: "beta-mgf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a positive [random variable](/D/rvar) following a [beta distribution](/D/gam):

$$ \label{eq:beta}
X \sim \mathrm{Bet}(\alpha, \beta) \; .
$$

Then, the [moment-generating function](/D/mgf) of $X$ is

$$ \label{eq:beta-mgf}
M_X(t) = 1 + \sum_{n=1}^{\infty} \left( \prod_{m=0}^{n-1} \frac{\alpha + m}{\alpha + \beta + m} \right) \frac{t^n}{n!} \; .
$$


**Proof:** The [probability density function of the beta distribution](/P/beta-pdf) is

$$ \label{eq:beta-pdf}
f_X(x) = \frac{1}{\mathrm{B}(\alpha, \beta)} \, x^{\alpha-1} \, (1-x)^{\beta-1}
$$

and the [moment-generating function](/D/mgf) is defined as

$$ \label{eq:mgf-var}
M_X(t) = \mathrm{E} \left[ e^{tX} \right] \; .
$$

Using the [expected value for continuous random variables](/D/mean), the moment-generating function of $X$ therefore is

$$ \label{eq:beta-mgf-s1}
\begin{split}
M_X(t) &= \int_{0}^{1} \exp[tx] \cdot \frac{1}{\mathrm{B}(\alpha, \beta)} \, x^{\alpha-1} \, (1-x)^{\beta-1} \, \mathrm{d}x \\
&= \frac{1}{\mathrm{B}(\alpha, \beta)} \int_{0}^{1} e^{tx} \, x^{\alpha-1} \, (1-x)^{\beta-1} \, \mathrm{d}x \; .
\end{split}
$$

With the relationship between beta function and gamma function

$$ \label{eq:beta-gam-fct}
\mathrm{B}(\alpha, \beta) = \frac{\Gamma(\alpha) \, \Gamma(\beta)}{\Gamma(\alpha+\beta)}
$$

and the integral representation of the confluent hypergeometric function (Kummer's function of the first kind)

$$ \label{eq:con-hyp-geo-fct-int}
{}_1 F_1(a,b,z) = \frac{\Gamma(b)}{\Gamma(a) \, \Gamma(b-a)} \int_{0}^{1} e^{zu} \, u^{a-1} \, (1-u)^{(b-a)-1} \, \mathrm{d}u \; ,
$$

the moment-generating function can be written as

$$ \label{eq:beta-mgf-s2}
M_X(t) = {}_1 F_1(\alpha,\alpha+\beta,t) \; .
$$

Note that the series equation for the confluent hypergeometric function (Kummer's function of the first kind) is

$$ \label{eq:con-hyp-geo-fct-ser}
{}_1 F_1(a,b,z) = \sum_{n=0}^{\infty} \frac{a^{\overline{n}}}{b^{\overline{n}}} \, \frac{z^n}{n!}
$$

where $m^{\overline{n}}$ is the rising factorial

$$ \label{eq:fact-rise}
m^{\overline{n}} = \prod_{i=0}^{n-1} (m+i) \; ,
$$

so that the moment-generating function can be written as

$$ \label{eq:beta-mgf-s3}
M_X(t) = \sum_{n=0}^{\infty} \frac{\alpha^{\overline{n}}}{(\alpha+\beta)^{\overline{n}}} \, \frac{t^n}{n!} \; .
$$

Applying the rising factorial equation \eqref{eq:fact-rise} and using $m^{\overline{0}} = x^0 = 0! = 1$, we finally have:

$$ \label{eq:beta-mgf-s4}
M_X(t) = 1 + \sum_{n=1}^{\infty} \left( \prod_{m=0}^{n-1} \frac{\alpha + m}{\alpha + \beta + m} \right) \frac{t^n}{n!} \; .
$$